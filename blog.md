---
layout: page
title: Blog
permalink: /blog/
---

<div class="blog-grid">
  {% assign articles = site.pages | filter: "layout", "post" %}
  {% for item in articles %}
  <article class="blog-card" style="border: 1px solid #eee; padding: 20px; margin-bottom: 20px; border-radius: 10px;">
    <div class="blog-card__content">
      <h2 class="blog-card__title">
        <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      </h2>
      <p class="blog-card__excerpt">
        {{ item.tldr | truncatewords: 20 }}
      </p>
      <a href="{{ item.url | relative_url }}" class="blog-card__link" style="color: orange; font-weight: bold;">Leggi la guida ➔</a>
    </div>
  </article>
  {% endfor %}
</div>
