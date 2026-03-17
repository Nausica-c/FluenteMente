---
layout: page
title: "Vocabolario Inglese: Liste di parole per livello (A1 - C1)"
description: "Tutte le liste di vocaboli divisi per livello."
permalink: /inglese/vocabolario/
---
<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>
<hr>

{% assign vocabolario_pages = site.pages | where_exp: "item", "item.categories contains 'inglese' and item.categories contains 'vocabolario'" %}
{% assign unclassified_pages = "" | split: "" %}
{% for item in vocabolario_pages %}
  {% unless item.categories contains 'a1' or item.categories contains 'a2' or item.categories contains 'b1' or item.categories contains 'b2' or item.categories contains 'c1' %}
    {% assign unclassified_pages = unclassified_pages | push: item %}
  {% endunless %}
{% endfor %}

{% if unclassified_pages.size > 0 %}
## 🆕 Nuovi arrivi (In aggiornamento)
<ul>
{% for item in unclassified_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small></li>
{% endfor %}
</ul><hr>
{% endif %}

## 🟢 Livello A1 (Principiante)
<ul>
{% assign a1_pages = site.pages | where_exp: "item", "item.categories contains 'inglese' and item.categories contains 'vocabolario' and item.categories contains 'a1'" %}
{% for item in a1_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small></li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato per il livello A1.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="vocabolario" lang="inglese" %}

<hr>
## 🟡 Livello A2 (Elementare) - *Coming Soon ⏳*
<hr>
## 🟠 Livello B1 (Intermedio) - *Coming Soon ⏳*
<hr>
## 🔴 Livello B2 (Intermedio Superiore) - *Coming Soon ⏳*
<hr>
## 🟣 Livello C1 (Avanzato) - *Coming Soon ⏳*
