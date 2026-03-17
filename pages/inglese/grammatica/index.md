---
layout: page
title: "Grammatica Inglese: Tutti gli articoli"
description: "Regole, eccezioni e spiegazioni semplici per padroneggiare la grammatica inglese senza impazzire."
permalink: /inglese/grammatica/
---

In questa pagina trovi l'archivio completo di tutte le guide e spiegazioni sulla grammatica inglese. Dimentica le noiose regole scolastiche: qui impariamo a usare la lingua vera.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign category_pages = site.pages | where_exp: "item", "item.categories contains 'inglese' and item.categories contains 'grammatica'" %}
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

{% include promo-box.html type="grammatica" lang="inglese" %}
