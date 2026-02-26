---
layout: page
title: "Errori Comuni in Inglese"
permalink: /inglese/errori/
---

# ⚠️ Errori Comuni in Inglese

False friends, parole ingannevoli e trappole tipiche degli italiani.

<ul>
{% assign items = site.pages | where_exp: "p", "p.url contains '/inglese/errori/'" | sort: "title" %}
{% for p in items %}
  {% if p.url != page.url and p.title %}
    <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
