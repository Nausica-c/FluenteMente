---
layout: page
title: "Frasi ed Espressioni in Francese: Tutti gli articoli"
description: "Archivio di frasi pronte all'uso ed espressioni utili in francese."
permalink: /francese/frasi/
---

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>
<hr>

<ul>
{% comment %} Filtro di sicurezza per evitare il crash sui nil {% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories != nil" %}
{% assign category_pages = safe_pages | where_exp: "item", "item.categories contains 'francese' and item.categories contains 'frasi'" %}

{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>
