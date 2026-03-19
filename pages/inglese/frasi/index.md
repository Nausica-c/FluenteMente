---
layout: page
title: "Frasi ed Espressioni in Inglese: Tutti gli articoli"
description: "Archivio di frasi pronte all'uso, espressioni per viaggiare e formule per sembrare più fluente."
permalink: /inglese/frasi/
---

Non sai come esprimerti in una certa situazione? In questo archivio trovi tutte le nostre guide dedicate alle frasi e alle espressioni di sopravvivenza in inglese, per lavoro o per i viaggi.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% comment %} 
Filtri a cascata per massima stabilità (evita l'errore "Expected end_of_string"):
1. Prendiamo solo le pagine che hanno l'attributo categories
2. Selezioniamo il cluster 'inglese'
3. Isoliamo la categoria 'frasi'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign en_pages = safe_pages | where_exp: "item", "item.categories contains 'inglese'" %}
{% assign category_pages = en_pages | where_exp: "item", "item.categories contains 'frasi'" %}

{% for item in category_pages %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">
      {% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>

{% include promo-box.html type="frasi" lang="inglese" %}
