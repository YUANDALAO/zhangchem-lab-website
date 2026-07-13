#!/usr/bin/env python3
"""
终极分子结构生成器
- 统一键长（所有分子大小一致）
- 纯黑白配色（无彩色）
- 细线条清晰
"""
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D
import yaml
import os
import argparse

# 配置
OUTPUT_DIR = 'assets/images/compounds'
YAML_FILE = '_data/molecules.yml'
IMAGE_SIZE = 400  # 正方形画布

# 绘图参数 - 精确控制
DRAW_OPTIONS = {
    'fixedBondLength': 30,           # 键长固定为30像素（关键！）
    'bondLineWidth': 1.2,            # 细线条
    'minFontSize': 12,               # 最小字体
    'maxFontSize': 14,               # 最大字体
    'atomLabelFontSize': 13,         # 原子标签字体
    'padding': 0.15,                 # 内边距
    'additionalAtomLabelPadding': 0.05,
}

# 黑白配色
BLACK = (0, 0, 0)       # 纯黑
WHITE = (1, 1, 1)       # 纯白

def load_molecules():
    """从YAML加载分子数据"""
    if not os.path.exists(YAML_FILE):
        print(f'❌ 找不到 {YAML_FILE}')
        return []
    
    with open(YAML_FILE, 'r', encoding='utf-8') as f:
        molecules = yaml.safe_load(f)
    
    return molecules if molecules else []

def generate_clean_svg(mol_id, smiles, output_dir):
    """生成统一键长的黑白SVG"""
    try:
        # 解析SMILES
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f'❌ {mol_id}: 无效的SMILES')
            return False
        
        # 生成2D坐标
        AllChem.Compute2DCoords(mol)
        
        # 创建SVG绘图器
        drawer = rdMolDraw2D.MolDraw2DSVG(IMAGE_SIZE, IMAGE_SIZE)
        
        # 设置绘图选项
        opts = drawer.drawOptions()
        
        # 关键：固定键长
        opts.fixedBondLength = DRAW_OPTIONS['fixedBondLength']
        opts.fixedScale = DRAW_OPTIONS['fixedBondLength']
        
        # 线条样式
        opts.bondLineWidth = DRAW_OPTIONS['bondLineWidth']
        
        # 字体大小
        opts.minFontSize = DRAW_OPTIONS['minFontSize']
        opts.maxFontSize = DRAW_OPTIONS['maxFontSize']
        opts.baseFontSize = DRAW_OPTIONS['atomLabelFontSize']
        
        # 内边距
        opts.padding = DRAW_OPTIONS['padding']
        opts.additionalAtomLabelPadding = DRAW_OPTIONS['additionalAtomLabelPadding']
        
        # 关键：使用黑白配色
        opts.useBWAtomPalette()  # RDKit内置的黑白调色板
        
        # 设置背景为白色
        opts.setBackgroundColour(WHITE)
        
        # 绘制分子
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        
        # 获取SVG
        svg = drawer.GetDrawingText()
        
        # 保存SVG
        svg_path = os.path.join(output_dir, f'{mol_id}.svg')
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(svg)
        
        print(f'✓ {mol_id}')
        return True
        
    except Exception as e:
        print(f'❌ {mol_id}: {str(e)}')
        return False

def main():
    parser = argparse.ArgumentParser(description='生成分子结构 SVG')
    parser.add_argument('--category', default=None, help='仅生成指定类别的分子 (如 scaffold)')
    args = parser.parse_args()

    print('='*60)
    print('🔬 终极分子结构生成器')
    print('='*60)
    
    # 加载分子
    molecules = load_molecules()
    if not molecules:
        print('\n❌ 没有找到分子数据！')
        print('请确保 _data/molecules.yml 存在并包含数据')
        return
    
    if args.category:
        molecules = [m for m in molecules if m.get('Category') == args.category]
        print(f'\n📊 找到 {len(molecules)} 个 {args.category} 分子')
    else:
        print(f'\n📊 找到 {len(molecules)} 个分子')
    print(f'📐 键长: {DRAW_OPTIONS["fixedBondLength"]}px (统一)')
    print(f'🖊️  线宽: {DRAW_OPTIONS["bondLineWidth"]}px (细线条)')
    print(f'🎨 配色: 黑白 (无彩色)\n')
    
    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 生成结构图
    success_count = 0
    failed = []
    
    for molecule in molecules:
        mol_id = molecule.get('ID', '')
        smiles = molecule.get('SMILES', '')
        
        if not mol_id or not smiles:
            continue
        
        if generate_clean_svg(mol_id, smiles, OUTPUT_DIR):
            success_count += 1
        else:
            failed.append(mol_id)
    
    # 总结
    print('\n' + '='*60)
    print(f'✅ 成功: {success_count}/{len(molecules)}')
    
    if failed:
        print(f'❌ 失败: {", ".join(failed)}')
    
    print(f'📂 输出: {OUTPUT_DIR}/')
    print('='*60)
    print('\n✨ 完成！所有分子键长统一、黑白清晰！')
    print('💡 现在可以在网页中使用这些SVG了')

if __name__ == '__main__':
    main()
