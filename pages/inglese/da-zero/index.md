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
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'da-zero'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">
      {% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% else %}
  <li><em>Nessun articolo ancora pubblicato in questa categoria.</em></li>
{% endfor %}
</ul>
