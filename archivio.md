---
layout: page
title: "Archivio"
permalink: /archivio/
---

<div class="archive-head">
  <h1 class="archive-title">📚 Archivio</h1>
  <p class="archive-subtitle">
    Scegli una lingua e poi un percorso. Le guide si aggiornano automaticamente quando aggiungi nuove pagine.
  </p>
</div>

{% assign languages = "inglese,spagnolo,francese,tedesco" | split: "," %}
{% assign sections = "da-zero,frasi,errori,pronuncia,curiosita" | split: "," %}

{% for lang in languages %}
  {% assign lang_root = '/' | append: lang | append: '/' %}
  {% assign lang_pages = site.pages | where_exp: "p", "p.url contains lang_root" %}

  {% if lang_pages.size > 0 %}
  <section class="archive-lang">
    <div class="archive-lang__header">
      <h2 class="archive-lang__title">🌍 {{ lang | capitalize }}</h2>
      <p class="archive-lang__meta">{{ lang_pages.size }} risorse</p>
    </div>

    <div class="archive-grid">
      {% for section in sections %}
        {% assign section_root = '/' | append: lang | append: '/' | append: section | append: '/' %}
        {% assign section_pages = site.pages | where_exp: "p", "p.url contains section_root" %}
        {% assign section_pages_sorted = section_pages | sort: "title" %}

        {% if section_pages.size > 0 %}
          <article class="archive-card">
            <div class="archive-card__top">
              <span class="archive-card__badge">
                {% case section %}
                  {% when "da-zero" %}📘 Da zero
                  {% when "frasi" %}💬 Frasi
                  {% when "errori" %}⚠️ Errori
                  {% when "pronuncia" %}🔊 Pronuncia
                  {% when "curiosita" %}🌍 Curiosità
                  {% else %}📌 {{ section | capitalize }}
                {% endcase %}
              </span>
              <span class="archive-card__count">{{ section_pages.size }}</span>
            </div>

            <h3 class="archive-card__title">
              {% case section %}
                {% when "da-zero" %}Inizia dalle basi
                {% when "frasi" %}Parla più naturale
                {% when "errori" %}Evita gli errori tipici
                {% when "pronuncia" %}Migliora l’accento
                {% when "curiosita" %}Inglese reale & sfumature
                {% else %}{{ section | replace:"-"," " | capitalize }}
              {% endcase %}
            </h3>

            <p class="archive-card__desc">
              {% case section %}
                {% when "da-zero" %}Guide per costruire fondamenta solide, anche se riparti da adulto.
                {% when "frasi" %}Espressioni utili, blocchi pronti e frasi che usano i madrelingua.
                {% when "errori" %}False friends, parole ingannevoli e trappole tipiche.
                {% when "pronuncia" %}Suoni difficili, parole problematiche e consigli pratici.
                {% when "curiosita" %}Idiomi, differenze culturali, britannico vs americano e altro.
                {% else %}Raccolta di risorse per questa sezione.
              {% endcase %}
            </p>

            <ul class="archive-card__list">
              {% assign shown = 0 %}
              {% for p in section_pages_sorted %}
                {% if p.title and p.url != page.url %}
                  <li class="archive-card__item">
                    <a class="archive-card__link" href="{{ p.url | relative_url }}">{{ p.title }}</a>
                  </li>
                  {% assign shown = shown | plus: 1 %}
                {% endif %}
                {% if shown == 6 %}{% break %}{% endif %}
              {% endfor %}
            </ul>

            <div class="archive-card__actions">
              <a class="archive-card__btn" href="{{ section_root | relative_url }}">
                Vedi tutto
              </a>
            </div>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>
  {% endif %}
{% endfor %}
