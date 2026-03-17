---
layout: page
title: "Inglese in Viaggio: L'archivio completo"
description: "Dal ristorante all'aeroporto: tutte le guide e le espressioni utili per viaggiare all'estero senza ansie."
permalink: /inglese/viaggio/
---

Le guide pratiche e i frasari per viaggiare in tutto il mondo in totale autonomia, usando l'inglese per cavartela in ogni situazione.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign category_pages = site.pages | where_exp: "item", "item.categories contains 'inglese' and item.categories contains 'viaggio'" %}
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
