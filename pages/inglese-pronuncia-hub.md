---
layout: page
title: "Pronuncia Inglese"
permalink: /inglese/pronuncia/
---

# 🔊 Pronuncia Inglese

Mini guide pratiche e parole difficili per italiani.

<ul>
{% assign items = site.pages | where_exp: "p", "p.url contains '/inglese/pronuncia/'" | sort: "title" %}
{% for p in items %}
  {% if p.url != page.url and p.title %}
    <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
