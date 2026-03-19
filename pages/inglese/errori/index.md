---
layout: page
title: "Errori e False Friends in Inglese: L'archivio"
description: "Scopri gli errori più comuni degli italiani in inglese e impara a riconoscere i temutissimi false friends."
permalink: /inglese/errori/
---

In questa pagina abbiamo raccolto tutti gli articoli che ti aiuteranno a non commettere più gli scivoloni tipici degli italiani quando parlano inglese. Conosci il tuo nemico (la traduzione letterale)!

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% comment %} 
Filtri a cascata per massima stabilità (evita l'errore "Expected end_of_string"):
1. Prendiamo solo le pagine che hanno categorie
2. Selezioniamo il cluster 'inglese'
3. Isoliamo la categoria 'errori'
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories" %}
{% assign en_pages = safe_pages | where_exp: "item", "item.categories contains 'inglese'" %}
{% assign category_pages = en_pages | where_exp: "item", "item.categories contains 'errori'" %}

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

{% include promo-box.html type="errori" lang="inglese" %}
