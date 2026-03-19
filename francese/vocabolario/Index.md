---
layout: page
title: "Vocabolario Francese: L'archivio completo"
description: "Tutte le liste di parole, verbi e sostantivi per arricchire il tuo francese."
permalink: /francese/vocabolario/
---

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>
<hr>

<ul>
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign fr_pages = safe_pages | where_exp: "item", "item.categories contains 'francese'" %}
{% assign category_pages = fr_pages | where_exp: "item", "item.categories contains 'vocabolario'" %}

{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="vocabolario" lang="francese" %}
