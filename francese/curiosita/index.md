---
layout: page
title: "Curiosità e Idiomi Francesi: L'archivio completo"
description: "Argot, verlan, idiomi intraducibili e tutta la cultura della lingua francese."
permalink: /francese/curiosita/
---

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>
<hr>

<ul>
{% comment %} 
Filtri concatenati per massima stabilità:
1. Filtriamo solo pagine che hanno categorie definite
2. Selezioniamo il cluster 'francese'
3. Isoliama la categoria 'curiosita'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign fr_pages = safe_pages | where_exp: "item", "item.categories contains 'francese'" %}
{% assign category_pages = fr_pages | where_exp: "item", "item.categories contains 'curiosita'" %}

{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="curiosita" lang="francese" %}
