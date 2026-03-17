---
layout: page
title: "Francese in Viaggio: L'archivio completo"
description: "Guide ed espressioni utili per viaggiare in Francia e nei paesi francofoni senza ansie."
permalink: /francese/viaggio/
---
<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>
<hr>
<ul>
{% assign category_pages = site.pages | where_exp: "item", "item.categories contains 'francese' and item.categories contains 'viaggio'" %}
{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>
{% include promo-box.html type="viaggio" lang="francese" %}
