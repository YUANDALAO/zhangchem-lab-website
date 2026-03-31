---
layout: default
title: Active Compound Library
permalink: /chemlib/active/
---

{% include lib-page-styles.html %}

<div class="lib-page-header lib-page-header--active">
  <a href="/chemlib/" class="lib-back">← ChemLib</a>
  <div class="lib-page-hero">
    <div class="lib-page-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    </div>
    <div>
      <div class="lib-page-tag">Library 01</div>
      <h1 class="lib-page-title">Active Compound Library</h1>
      <p class="lib-page-desc">Screened and validated bioactive compounds with confirmed target activity. Each compound has been experimentally tested and confirmed for activity against one or more biological targets — ideal starting points for hit-to-lead optimization.</p>
      <div class="lib-page-tags">
        <span>Hit compounds</span>
        <span>Validated activity</span>
        <span>Biological targets</span>
      </div>
    </div>
  </div>
</div>

{% include library_list.html category="active" %}

<style>
.lib-page-header--active {
  --accent: #2563eb;
  --accent-bg: #eff6ff;
  --accent-border: #bfdbfe;
  --tag-bg: #dbeafe;
  --tag-color: #1d4ed8;
  --icon-bg: #dbeafe;
}
</style>
