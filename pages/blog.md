---
layout: page
title: Tutti gli Articoli
subtitle: Esplora le nostre guide, i trucchi di produttività e il vocabolario essenziale per imparare le lingue senza stress.
permalink: /blog/
---

<div class="archive-grid" style="margin-top: 40px;">
  {% for post in site.posts %}
  <a href="{{ post.url | relative_url }}" class="archive-card" style="text-decoration: none;">
    <div class="archive-card__top">
      <span class="archive-card__badge">{{ post.date | date: "%d/%m/%Y" }}</span>
    </div>
    <h3 class="archive-card__title">{{ post.title }}</h3>
    {% if post.tldr %}
      <p class="archive-card__desc">{{ post.tldr | truncatewords: 20 }}</p>
    {% endif %}
    <span style="color: var(--primary-color); font-weight: 800; font-size: 0.9rem;">Leggi l'articolo ➔</span>
  </a>
  {% endfor %}
</div>
