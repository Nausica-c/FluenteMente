---
layout: page
title: "Business English: Tutti gli articoli per il lavoro"
description: "L'archivio completo per imparare l'inglese professionale: email, call, riunioni e colloqui."
permalink: /inglese/business/
---

Tutte le risorse per migliorare il tuo inglese professionale e aprirti nuove opportunità di carriera a livello internazionale.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% comment %} Filtro di sicurezza per evitare il crash sui valori nulli (nil) {% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories != nil" %}
{% assign category_pages = safe_pages | where_exp: "item", "item.categories contains 'inglese' and item.categories contains 'business'" %}

{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">
      {% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="business" lang="inglese" %}
