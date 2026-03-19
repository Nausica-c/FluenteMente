---
layout: page
title: "Inglese da Zero: Tutti gli articoli per iniziare"
description: "Tutte le nostre guide per chi parte da zero con l'inglese, per superare i blocchi mentali e iniziare a parlare."
permalink: /inglese/da-zero/
---

In questa pagina trovi l'archivio completo di tutti i nostri articoli dedicati a chi si approccia all'inglese da adulto. Dal mindset giusto, a come sbloccare il parlato, fino al metodo di studio.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% comment %} 
Filtri a cascata per massima stabilità:
1. Prendiamo solo le pagine che hanno categorie
2. Selezioniamo il cluster 'inglese'
3. Isoliamo la categoria 'da-zero'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign en_pages = safe_pages | where_exp: "item", "item.categories contains 'inglese'" %}
{% assign category_pages = en_pages | where_exp: "item", "item.categories contains 'da-zero'" %}

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

{% include promo-box.html type="da-zero" lang="inglese" %}
