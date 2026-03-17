---
layout: page
title: "Francese da Zero: Tutti gli articoli per iniziare"
description: "Tutte le nostre guide per chi parte da zero con il francese."
permalink: /francese/da-zero/
---
<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>
<hr>
<ul>
{% assign category_pages = site.pages | where_exp: "item", "item.categories contains 'francese' and item.categories contains 'da-zero'" %}
{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>
