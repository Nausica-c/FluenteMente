---
layout: page
title: "Curiosità e Idiomi Francesi: L'archivio completo"
description: "Argot, verlan, slang giovanile, idiomi intraducibili e tutta la cultura dietro la lingua francese."
permalink: /francese/curiosita/
---

Qui trovi tutto il materiale per andare oltre la grammatica: scopri le abitudini dei francesi, le espressioni intraducibili e lo slang locale che renderanno il tuo francese super autentico.

<a href="{{ '/francese/' | relative_url }}">⬅ Torna alla guida principale di Francese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'francese' and post.categories contains 'curiosita'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">{% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>
