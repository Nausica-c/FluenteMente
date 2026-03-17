---
layout: page
title: "Curiosità e Idiomi Inglesi: L'archivio completo"
description: "Modi di dire, slang, differenze tra inglese americano e britannico e tutta la cultura dietro la lingua."
permalink: /inglese/curiosita/
---

Qui trovi tutto il materiale per andare oltre la semplice grammatica: slang, idiomi intraducibili e differenze culturali che renderanno il tuo inglese molto più autentico e simile a quello dei madrelingua.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign category_pages = site.pages | where_exp: "item", "item.categories contains 'inglese' and item.categories contains 'curiosita'" %}
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
