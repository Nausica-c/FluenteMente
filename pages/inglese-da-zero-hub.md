---
layout: page
title: "Inglese da Zero"
permalink: /inglese/da-zero/
---

# 📘 Inglese da Zero

Qui trovi le guide per iniziare da adulto con un percorso chiaro.

<ul>
{% assign items = site.pages | where_exp: "p", "p.url contains '/inglese/da-zero/'" | sort: "title" %}
{% for p in items %}
  {% if p.url != page.url and p.title %}
    <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

<p style="margin-top:16px;">
  👉 Se vuoi una struttura chiara: <a href="{{ '/metodo-consigliato/' | relative_url }}">Metodo consigliato</a>
</p>
