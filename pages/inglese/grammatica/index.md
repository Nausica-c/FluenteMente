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
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'grammatica'" %}
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

{% include promo-box.html type="grammatica" lang="inglese" %}
