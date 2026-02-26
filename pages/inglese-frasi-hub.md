---
layout: page
title: "Frasi Inglesi"
permalink: /inglese/frasi/
---

# 💬 Frasi Inglesi

Frasi utili, espressioni reali e blocchi pronti per parlare più naturale.

<ul>
{% assign items = site.pages | where_exp: "p", "p.url contains '/inglese/frasi/'" | sort: "title" %}
{% for p in items %}
  {% if p.url != page.url and p.title %}
    <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
