---
layout: page
title: "Inglese in Viaggio: L'archivio completo"
description: "Tutte le risorse per viaggiare senza ansie: aeroporto, hotel, ristorante e indicazioni stradali."
permalink: /inglese/viaggio/
---

In questa sezione trovi tutte le nostre guide pratiche per affrontare i tuoi viaggi all'estero con sicurezza, gestendo ogni situazione: dal check-in in aeroporto all'ordinazione al ristorante.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>
<hr>

<ul>
{% comment %} 
Filtri concatenati per la massima stabilità (evita l'errore "Expected end_of_string"):
1. Prendiamo solo le pagine che hanno l'attributo categories
2. Selezioniamo il cluster 'inglese'
3. Isoliamo la categoria 'viaggio'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign en_pages = safe_pages | where_exp: "item", "item.categories contains 'inglese'" %}
{% assign category_pages = en_pages | where_exp: "item", "item.categories contains 'viaggio'" %}

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

{% include promo-box.html type="viaggio" lang="inglese" %}
