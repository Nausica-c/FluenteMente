---
layout: page
title: Archivio Guide Pratiche
subtitle: Esplora tutti i nostri contenuti su metodo, vocabolario e strumenti per imparare le lingue senza stress.
permalink: /blog/
---

<div class="blog-grid">
  {% for post in site.posts %}
  <article class="blog-card">
    <div class="blog-card__content">
      <div class="blog-card__meta">
        <span class="blog-card__date">{{ post.date | date: "%d/%m/%Y" }}</span>
        {% if post.categories %}
          <span class="blog-card__category">{{ post.categories | first }}</span>
        {% endif %}
      </div>
      <h2 class="blog-card__title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      <p class="blog-card__excerpt">
        {% if post.tldr %}
          {{ post.tldr | truncatewords: 20 }}
        {% else %}
          {{ post.content | strip_html | truncatewords: 20 }}
        {% endif %}
      </p>
      <a href="{{ post.url | relative_url }}" class="blog-card__link">Leggi la guida ➔</a>
    </div>
  </article>
  {% endfor %}
</div>

{% include orient-box.html text="Non sai da quale lingua iniziare o cerchi lo strumento giusto? Guarda la nostra selezione delle migliori app dell'anno." %}
