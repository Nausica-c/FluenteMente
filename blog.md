<div class="blog-grid">
  {% assign articles = site.pages | filter: "layout", "post" | sort: "date" | reverse %}
  {% for item in articles %}
  <article class="blog-card">
    <div class="blog-card__content">
      <div class="blog-card__meta">
        <span class="blog-card__date">{{ item.date | date: "%d/%m/%Y" }}</span>
        {% if item.categories %}
          <span class="blog-card__category">{{ item.categories | first }}</span>
        {% endif %}
      </div>
      <h2 class="blog-card__title">
        <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
      </h2>
      <p class="blog-card__excerpt">
        {% if item.tldr %}
          {{ item.tldr | truncatewords: 20 }}
        {% else %}
          {{ item.content | strip_html | truncatewords: 20 }}
        {% endif %}
      </p>
      <a href="{{ item.url | relative_url }}" class="blog-card__link">Leggi la guida ➔</a>
    </div>
  </article>
  {% endfor %}
</div>
