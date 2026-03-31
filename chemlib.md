---
layout: default
title: ChemLib
permalink: /chemlib/
nav_order: 4
---

<div class="chemlib-hero">
  <div class="chemlib-hero-content">
    <div class="chemlib-badge">Compound Libraries</div>
    <h1 class="chemlib-title">ZhangLab ChemLib</h1>
    <p class="chemlib-subtitle">Curated collections of bioactive small molecules for drug discovery and chemical biology research</p>
    <div class="chemlib-stats">
      <div class="stat-item">
        <span class="stat-number">726+</span>
        <span class="stat-label">Compounds</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <span class="stat-number">4</span>
        <span class="stat-label">Libraries</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <span class="stat-number">SVG</span>
        <span class="stat-label">Structures</span>
      </div>
    </div>
  </div>
</div>

<div class="library-grid">

  <a href="/chemlib/active/" class="library-card library-card--active">
    <div class="library-card-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    </div>
    <div class="library-card-body">
      <div class="library-card-tag">Library 01</div>
      <h2 class="library-card-title">Active Compound Library</h2>
      <p class="library-card-desc">Screened and validated bioactive compounds with confirmed target activity. Ideal starting points for hit-to-lead optimization.</p>
      <div class="library-card-meta">
        <span class="meta-tag">Hit compounds</span>
        <span class="meta-tag">Validated activity</span>
      </div>
    </div>
    <div class="library-card-arrow">Browse →</div>
  </a>

  <a href="/chemlib/natural/" class="library-card library-card--natural">
    <div class="library-card-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M12 2a9 9 0 00-9 9c0 4.17 2.84 7.67 6.69 8.69L12 22l2.31-2.31C18.16 18.67 21 15.17 21 11a9 9 0 00-9-9z"/>
        <path d="M12 6v6l4 2"/>
      </svg>
    </div>
    <div class="library-card-body">
      <div class="library-card-tag">Library 02</div>
      <h2 class="library-card-title">Natural Product Library</h2>
      <p class="library-card-desc">Plant, microbial, and marine-derived natural products and semi-synthetic derivatives with broad chemical diversity.</p>
      <div class="library-card-meta">
        <span class="meta-tag">Natural origin</span>
        <span class="meta-tag">Broad diversity</span>
      </div>
    </div>
    <div class="library-card-arrow">Browse →</div>
  </a>

  <a href="/chemlib/scaffold/" class="library-card library-card--scaffold">
    <div class="library-card-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M12 2L2 7l10 5 10-5-10-5z"/>
        <path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>
      </svg>
    </div>
    <div class="library-card-body">
      <div class="library-card-tag">Library 03</div>
      <h2 class="library-card-title">Novel Scaffold Library</h2>
      <p class="library-card-desc">In-house synthesized compounds featuring unique heterocyclic scaffolds not represented in commercial collections.</p>
      <div class="library-card-meta">
        <span class="meta-tag">Novel scaffolds</span>
        <span class="meta-tag">In-house synthesis</span>
      </div>
    </div>
    <div class="library-card-arrow">Browse →</div>
  </a>

  <a href="/chemlib/druglike/" class="library-card library-card--druglike">
    <div class="library-card-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
      </svg>
    </div>
    <div class="library-card-body">
      <div class="library-card-tag">Library 04</div>
      <h2 class="library-card-title">Drug‑Like Library</h2>
      <p class="library-card-desc">High-diversity small molecules satisfying Lipinski's Rule of Five. Optimized for oral bioavailability and drug-like properties.</p>
      <div class="library-card-meta">
        <span class="meta-tag">Lipinski compliant</span>
        <span class="meta-tag">High diversity</span>
      </div>
    </div>
    <div class="library-card-arrow">Browse →</div>
  </a>

</div>

<style>
/* ── Hero ─────────────────────────────────────────────── */
.chemlib-hero {
  background: linear-gradient(135deg, #1a2332 0%, #2c3e50 50%, #3d5a80 100%);
  border-radius: 20px;
  padding: 60px 48px;
  margin-bottom: 48px;
  position: relative;
  overflow: hidden;
}
.chemlib-hero::before {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(139,156,182,0.15) 0%, transparent 70%);
  border-radius: 50%;
}
.chemlib-hero::after {
  content: '';
  position: absolute;
  bottom: -80px; left: 40%;
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(61,90,128,0.2) 0%, transparent 70%);
  border-radius: 50%;
}
.chemlib-hero-content { position: relative; z-index: 1; }
.chemlib-badge {
  display: inline-block;
  background: rgba(139,156,182,0.2);
  border: 1px solid rgba(139,156,182,0.35);
  color: #a8bbd4;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 5px 14px;
  border-radius: 20px;
  margin-bottom: 20px;
}
.chemlib-title {
  font-size: 42px;
  font-weight: 700;
  color: #f0f4f8;
  margin: 0 0 16px;
  line-height: 1.15;
}
.chemlib-subtitle {
  font-size: 16px;
  color: #8a9bb5;
  max-width: 560px;
  line-height: 1.7;
  margin: 0 0 36px;
}
.chemlib-stats {
  display: flex;
  align-items: center;
  gap: 0;
}
.stat-item {
  display: flex;
  flex-direction: column;
  padding: 0 28px;
}
.stat-item:first-child { padding-left: 0; }
.stat-number {
  font-size: 28px;
  font-weight: 700;
  color: #c8d8ea;
  line-height: 1;
}
.stat-label {
  font-size: 12px;
  color: #6b7d91;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 4px;
}
.stat-divider {
  width: 1px;
  height: 36px;
  background: rgba(139,156,182,0.25);
}

/* ── Library Grid ─────────────────────────────────────── */
.library-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}
.library-card {
  display: flex;
  flex-direction: column;
  border-radius: 16px;
  padding: 32px;
  text-decoration: none;
  border: 1px solid transparent;
  transition: all 0.25s ease;
  position: relative;
  overflow: hidden;
}
.library-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  border-radius: 16px 16px 0 0;
}
.library-card--active  { background: #f0f7ff; border-color: #c5ddf7; }
.library-card--active::before  { background: linear-gradient(90deg, #3b82f6, #60a5fa); }
.library-card--natural { background: #f0fdf4; border-color: #bbf7d0; }
.library-card--natural::before { background: linear-gradient(90deg, #16a34a, #4ade80); }
.library-card--scaffold{ background: #fff7ed; border-color: #fed7aa; }
.library-card--scaffold::before{ background: linear-gradient(90deg, #ea580c, #fb923c); }
.library-card--druglike{ background: #faf5ff; border-color: #e9d5ff; }
.library-card--druglike::before{ background: linear-gradient(90deg, #9333ea, #c084fc); }

.library-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}
.library-card--active:hover  { border-color: #93c5fd; }
.library-card--natural:hover { border-color: #86efac; }
.library-card--scaffold:hover{ border-color: #fdba74; }
.library-card--druglike:hover{ border-color: #d8b4fe; }

.library-card-icon {
  width: 48px; height: 48px;
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 20px;
  flex-shrink: 0;
}
.library-card--active  .library-card-icon { background: #dbeafe; color: #2563eb; }
.library-card--natural .library-card-icon { background: #dcfce7; color: #16a34a; }
.library-card--scaffold .library-card-icon{ background: #ffedd5; color: #ea580c; }
.library-card--druglike .library-card-icon{ background: #f3e8ff; color: #9333ea; }
.library-card-icon svg { width: 24px; height: 24px; }

.library-card-body { flex: 1; }
.library-card-tag {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.library-card--active  .library-card-tag { color: #2563eb; }
.library-card--natural .library-card-tag { color: #16a34a; }
.library-card--scaffold .library-card-tag{ color: #ea580c; }
.library-card--druglike .library-card-tag{ color: #9333ea; }

.library-card-title {
  font-size: 19px;
  font-weight: 700;
  color: #1e2a3a;
  margin: 0 0 12px;
  line-height: 1.3;
}
.library-card-desc {
  font-size: 14px;
  color: #4a5568;
  line-height: 1.7;
  margin: 0 0 20px;
}
.library-card-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
}
.meta-tag {
  font-size: 12px;
  padding: 4px 10px;
  border-radius: 20px;
  font-weight: 500;
}
.library-card--active  .meta-tag { background: #dbeafe; color: #1d4ed8; }
.library-card--natural .meta-tag { background: #dcfce7; color: #15803d; }
.library-card--scaffold .meta-tag{ background: #ffedd5; color: #c2410c; }
.library-card--druglike .meta-tag{ background: #f3e8ff; color: #7c3aed; }

.library-card-arrow {
  font-size: 14px;
  font-weight: 600;
  opacity: 0.6;
  transition: opacity 0.2s, transform 0.2s;
}
.library-card:hover .library-card-arrow {
  opacity: 1;
  transform: translateX(4px);
}
.library-card--active  .library-card-arrow { color: #2563eb; }
.library-card--natural .library-card-arrow { color: #16a34a; }
.library-card--scaffold .library-card-arrow{ color: #ea580c; }
.library-card--druglike .library-card-arrow{ color: #9333ea; }

/* ── Responsive ───────────────────────────────────────── */
@media (max-width: 900px) {
  .library-grid { grid-template-columns: 1fr; }
  .chemlib-title { font-size: 32px; }
  .chemlib-hero { padding: 40px 28px; }
}
@media (max-width: 600px) {
  .chemlib-stats { flex-wrap: wrap; gap: 16px; }
  .stat-divider { display: none; }
  .stat-item { padding: 0; }
}
</style>
