---
layout: page
title: "Curiosità e Idiomi Inglesi: L'archivio completo"
description: "Modi di dire, slang, differenze tra inglese americano e britannico e tutta la cultura dietro la lingua."
permalink: /inglese/curiosita/
---

Qui trovi tutto il materiale per andare oltre la grammatica: slang, idiomi e differenze culturali che renderanno il tuo inglese molto più autentico.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'curiosita'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">
      {% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% endfor %}
</ul>
