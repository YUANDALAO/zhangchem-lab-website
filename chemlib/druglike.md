---
layout: default
title: Approved Drug Library
permalink: /chemlib/druglike/
---

{% include lib-page-styles.html %}

<div class="lib-page-header lib-page-header--druglike">
  <a href="/chemlib/" class="lib-back">← ChemLib</a>
  <div class="lib-page-hero">
    <div class="lib-page-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
        <path d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
      </svg>
    </div>
    <div>
      <div class="lib-page-tag">Library 04</div>
      <h1 class="lib-page-title">Approved Drug Library</h1>
      <p class="lib-page-desc">FDA and globally approved drugs spanning diverse disease indications. This collection enables drug repurposing studies, mechanistic research, and target identification using clinically validated compounds.</p>
      <div class="lib-page-tags">
        <span>FDA approved</span>
        <span>Drug repurposing</span>
        <span>Clinical indications</span>
      </div>
    </div>
  </div>
</div>

{% include library_list.html category="druglike" %}

<style>
.lib-page-header--druglike {
  --accent: #9333ea;
  --accent-bg: #faf5ff;
  --accent-border: #e9d5ff;
  --tag-bg: #f3e8ff;
  --tag-color: #7c3aed;
  --icon-bg: #f3e8ff;
}
</style>
