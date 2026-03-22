---
layout: page
title: Archivio Guide Pratiche
permalink: /blog/
---

<style>
/* CSS specifico per la griglia del blog */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.blog-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: none; /* Nascondiamo tutto, lo gestisce il JS sotto */
    flex-direction: column;
    overflow: hidden;
    padding: 25px;
}

.blog-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
}

.blog-card__meta {
    font-size: 0.8rem;
    color: #718096;
    margin-bottom: 10px;
    text-transform: uppercase;
}

.blog-card__title {
    font-size: 1.3rem;
    margin-bottom: 15px;
    line-height: 1.3;
}

.blog-card__title a {
    text-decoration: none;
    color: var(--secondary-color, #2d3748);
}

.blog-card__excerpt {
    font-size: 0.95rem;
    color: #4a5568;
    line-height: 1.6;
    margin-bottom: 20px;
}

.blog-card__link {
    font-weight: 700;
    color: var(--primary-color, #f6ad55);
    text-decoration: none;
}

#load-more-container {
    text-align: center;
    margin: 50px 0;
}

.btn-load-more {
    background-color: var(--secondary-color, #2d3748);
    color: white;
    padding: 15px 30px;
    border-radius: 50px;
    border: none;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s;
}

.btn-load-more:hover {
    background-color: var(--primary-color, #f6ad55);
}
</style>

<div class="blog-grid" id="blog-grid">
  {% assign articles = site.pages | where: "layout", "post" | sort: "date" | reverse %}
  {% for item in articles %}
  <article class="blog-card">
    <div class="blog-card__meta">
      {{ item.date | date: "%d/%m/%Y" }}
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
  </article>
  {% endfor %}
</div>

<div id="load-more-container">
  <button id="load-more" class="btn-load-more">Carica altri articoli</button>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const itemsPerPage = 6; // Quanti articoli mostrare per volta
    const items = Array.from(document.querySelectorAll('.blog-card'));
    const loadMoreBtn = document.getElementById('load-more');
    let currentIndex = 0;

    function showNextItems() {
        const nextSet = items.slice(currentIndex, currentIndex + itemsPerPage);
        nextSet.forEach(item => {
            item.style.display = 'flex'; // Mostriamo le card come flexbox
        });
        currentIndex += itemsPerPage;

        // Se non ci sono più articoli, nascondiamo il tasto
        if (currentIndex >= items.length) {
            document.getElementById('load-more-container').style.display = 'none';
        }
    }

    // Mostra il primo set all'avvio
    showNextItems();

    // Evento al click
    loadMoreBtn.addEventListener('click', showNextItems);
});
</script>
