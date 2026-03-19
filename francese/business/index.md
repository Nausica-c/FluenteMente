---
layout: page
title: "Francese per il Lavoro: L'archivio completo"
description: "Migliora il tuo francese professionale: email, call, riunioni e colloqui."
permalink: /francese/business/
---

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>
<hr>

<ul>
{% comment %} 
Applichiamo i filtri in cascata per evitare errori di sintassi:
1. Filtriamo le pagine che hanno categorie
2. Filtriamo per 'francese'
3. Filtriamo per 'business'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign fr_pages = safe_pages | where_exp: "item", "item.categories contains 'francese'" %}
{% assign category_pages = fr_pages | where_exp: "item", "item.categories contains 'business'" %}

{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="business" lang="francese" %}
