---
layout: page
title: "Vocabolario Inglese: Liste di parole per livello (A1 - C1)"
description: "Tutte le liste di vocaboli divisi per livello."
permalink: /inglese/vocabolario/
---

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>
<hr>

{% comment %} 
SCUDO DI SICUREZZA: 
1. Filtriamo solo le pagine che hanno categorie
2. Isoliama il cluster 'inglese'
3. Isoliamo la sezione 'vocabolario'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign en_pages = safe_pages | where_exp: "item", "item.categories contains 'inglese'" %}
{% assign vocabolario_pages = en_pages | where_exp: "item", "item.categories contains 'vocabolario'" %}

{% comment %} Logica per identificare pagine senza un livello specifico (A1-C1) {% endcomment %}
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
{% assign a1_pages = vocabolario_pages | where_exp: "item", "item.categories contains 'a1'" %}
{% for item in a1_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small></li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

<hr>

## 🟡 Livello A2 (Pre-Intermedio)
<ul>
{% assign a2_pages = vocabolario_pages | where_exp: "item", "item.categories contains 'a2'" %}
{% for item in a2_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small></li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

<hr>

## 🟠 Livelli B1 / B2 (Intermedio)
<ul>
{% comment %} Per i livelli combinati B1/B2, filtriamo separatamente e uniamo i risultati {% endcomment %}
{% assign b1_pages = vocabolario_pages | where_exp: "item", "item.categories contains 'b1'" %}
{% assign b2_pages = vocabolario_pages | where_exp: "item", "item.categories contains 'b2'" %}
{% assign b_pages = b1_pages | concat: b2_pages | uniq %}

{% for item in b_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small></li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

<hr>

## 🔴 Livello C1 (Avanzato)
<ul>
{% assign c1_pages = vocabolario_pages | where_exp: "item", "item.categories contains 'c1'" %}
{% for item in c1_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small></li>
{% else %}
  <li><em>Nessun articolo per questo livello.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="vocabolario" lang="inglese" %}
