import pandas as pd
import yaml
import json
import os
from collections import Counter

# --- Config ---
SOURCE_FOLDER   = '_chemlib_data'
OUTPUT_YAML     = '_data/molecules.yml'
OUTPUT_JSON_DIR = 'assets/data'

# Libraries with <= this many compounds stay in molecules.yml (Jekyll/Liquid)
YAML_SIZE_LIMIT = 3000

CATEGORY_KEYWORDS = [
    ('natural',   'natural'),
    ('active',    'active'),
    ('druglike',  'druglike'),
    ('drug_like', 'druglike'),
    ('drug-like', 'druglike'),
    ('scaffold',  'scaffold'),
]

def detect_category(filename):
    name_lower = filename.lower()
    for keyword, category in CATEGORY_KEYWORDS:
        if keyword in name_lower:
            return category
    return 'unknown'

def read_sheet(path):
    """Try 'Compound List' sheet, then 'Sheet1', then first sheet."""
    xl = pd.ExcelFile(path)
    for sheet in ['Compound List', 'Sheet1']:
        if sheet in xl.sheet_names:
            return pd.read_excel(path, sheet_name=sheet)
    return pd.read_excel(path, sheet_name=xl.sheet_names[0])

def normalise_columns(df):
    """Rename variant column names to canonical ones."""
    renames = {}
    cols = df.columns.tolist()

    # ID: prefer 'No.' then 'IDNUMBER' then 'ID'
    if 'ID' not in cols:
        if 'No.' in cols:
            renames['No.'] = 'ID'
        elif 'IDNUMBER' in cols:
            renames['IDNUMBER'] = 'ID'

    # MW: prefer 'MW' then 'MolWt'
    if 'MW' not in cols and 'MolWt' in cols:
        renames['MolWt'] = 'MW'

    # Name
    if 'name' not in cols and 'MOLENAME' in cols:
        renames['MOLENAME'] = 'name'

    # Subcategory: 'Library' / 'category' / 'Disease' → 'subcategory'
    if 'subcategory' not in cols:
        for col in ['Library', 'category', 'Disease']:
            if col in cols:
                renames[col] = 'subcategory'
                break

    return df.rename(columns=renames)

def process_files():
    all_molecules = []

    print(f"Scanning: {SOURCE_FOLDER}\n")
    if not os.path.isdir(SOURCE_FOLDER):
        print(f"[Error] Folder '{SOURCE_FOLDER}' not found.")
        return

    for filename in sorted(os.listdir(SOURCE_FOLDER)):
        if not filename.endswith('.xlsx') or filename.startswith('~'):
            continue

        file_path = os.path.join(SOURCE_FOLDER, filename)
        category  = detect_category(filename)
        print(f"  {filename}  →  category = '{category}'")

        try:
            df = read_sheet(file_path)
            df = normalise_columns(df)

            if 'ID' not in df.columns or 'SMILES' not in df.columns:
                print(f"    [Warning] Missing ID or SMILES — skipped.")
                print(f"    Columns: {df.columns.tolist()}")
                continue

            # Use Category column from Excel if it overrides filename-detected category
            if 'Category' in df.columns:
                df['_cat'] = df['Category'].fillna(category).astype(str).str.strip().str.lower()
            else:
                df['_cat'] = category

            count = 0
            for _, row in df.iterrows():
                if pd.isna(row['ID']) or pd.isna(row['SMILES']):
                    continue

                mol = {
                    'ID':       str(row['ID']).strip(),
                    'SMILES':   str(row['SMILES']).strip(),
                    'Category': row['_cat'],
                }
                if 'MW' in df.columns and pd.notna(row.get('MW')):
                    mol['MW'] = round(float(row['MW']), 2)
                if 'name' in df.columns and pd.notna(row.get('name')):
                    mol['name'] = str(row['name']).strip()
                if 'subcategory' in df.columns and pd.notna(row.get('subcategory')):
                    mol['subcategory'] = str(row['subcategory']).strip()

                all_molecules.append(mol)
                count += 1

            print(f"    {count} compounds loaded")

        except Exception as e:
            import traceback
            print(f"    [Error] {e}")
            traceback.print_exc()

    if not all_molecules:
        print("\n[Warning] No molecule data found.")
        return

    # ── Group by category ──────────────────────────────────
    cats = Counter(m['Category'] for m in all_molecules)
    by_category = {}
    for mol in all_molecules:
        by_category.setdefault(mol['Category'], []).append(mol)

    print(f"\nTotal: {len(all_molecules)} compounds")
    print("  Category breakdown:")
    for cat, count in sorted(cats.items()):
        print(f"    {cat:12s}: {count}")

    # ── Write per-category JSON ────────────────────────────
    os.makedirs(OUTPUT_JSON_DIR, exist_ok=True)
    for cat, mols in sorted(by_category.items()):
        json_path = os.path.join(OUTPUT_JSON_DIR, f"compounds_{cat}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(mols, f, ensure_ascii=False, separators=(',', ':'))
        size_kb = os.path.getsize(json_path) // 1024
        print(f"  → {json_path}  ({len(mols)} compounds, {size_kb} KB)")

    # ── Write molecules.yml (small libs only, for Jekyll) ──
    yaml_mols = [m for m in all_molecules if cats[m['Category']] <= YAML_SIZE_LIMIT]
    os.makedirs(os.path.dirname(OUTPUT_YAML), exist_ok=True)
    with open(OUTPUT_YAML, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_mols, f,
                  default_flow_style=False,
                  allow_unicode=True,
                  sort_keys=False)
    print(f"\n  molecules.yml: {len(yaml_mols)} compounds (libs ≤ {YAML_SIZE_LIMIT})")

if __name__ == '__main__':
    process_files()
