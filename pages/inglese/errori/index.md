---
layout: page
title: "Errori e False Friends in Inglese: L'archivio"
description: "Scopri gli errori più comuni degli italiani in inglese e impara a riconoscere i temutissimi false friends."
permalink: /inglese/errori/
---

In questa pagina abbiamo raccolto tutti gli articoli che ti aiuteranno a non commettere più gli scivoloni tipici degli italiani quando parlano inglese.

<a href="{{ '/inglese/' | relative_url }}">⬅ Torna alla guida principale di Inglese</a>

<hr>

<ul>
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'inglese' and post.categories contains 'errori'" %}
{% for post in category_posts %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong>
    <br><small style="color: #555;">
      {% if post.description %}{{ post.description }}{% else %}{{ post.excerpt | strip_html | truncatewords: 25 }}{% endif %}
    </small>
  </li>
{% endfor %}
</ul>

{% include promo-box.html type="errori" lang="inglese" %}
