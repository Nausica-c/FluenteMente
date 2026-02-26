---
layout: page
title: "Curiosità Linguistiche Inglese"
permalink: /inglese/curiosita/
---

# 🌍 Curiosità Linguistiche Inglese

Idiomi, parole intraducibili, differenze UK vs US e inglese “reale”.

<ul>
{% assign items = site.pages | where_exp: "p", "p.url contains '/inglese/curiosita/'" | sort: "title" %}
{% for p in items %}
  {% if p.url != page.url and p.title %}
    <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
