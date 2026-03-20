 ---
layout: page
title: "Archivio completo degli articoli"
subtitle: "Tutte le nostre guide, le recensioni e i trucchi per imparare le lingue."
description: "Esplora l'archivio completo di FluenteMente. Trova tutte le guide su inglese, spagnolo, francese e recensioni delle migliori app."
permalink: /archivio/
bridge_type: base

next_title: "Hai trovato quello che cercavi?"
next_text: "Dopo aver esplorato l’archivio, il passo più utile è scegliere un percorso chiaro: partire dal metodo, confrontare gli strumenti o tornare all’hub principale delle lingue."
next_cta1: "Leggi il metodo consigliato"
next_url1: "/metodo-consigliato/"
next_cta2: "Vai all’hub lingue"
next_url2: "/hub-lingue/"
next_micro: "Se invece vuoi confrontare subito gli strumenti,"
next_microlink: "/babbel-vs-duolingo/"
next_microanchor: "leggi il confronto Babbel vs Duolingo"
---

{% comment %}
Uniamo pagine e articoli in un'unica collezione e ordiniamo per titolo.
{% endcomment %}
{% assign all_content = site.pages | concat: site.posts %}
{% assign sorted_content = all_content | sort: "title" %}

Benvenuto nella libreria completa di **FluenteMente**. Qui trovi ogni singola guida e analisi pubblicata sul sito, organizzata per lingua e argomento per facilitarti la ricerca.

### Esplora per categoria
[**Metodo e App**](#metodo) | [**🇬🇧 Inglese**](#inglese) | [**🇫🇷 Francese**](#francese) | [**🇪🇸 Spagnolo / 🇩🇪 Tedesco / 🇧🇷 Portoghese**](#altre-lingue)

---

<h2 id="metodo">🚀 Metodo di Studio e Recensioni App</h2>
<p>Le guide fondamentali per approcciare qualsiasi lingua e le nostre analisi sugli strumenti digitali.</p>

<ul>
{% for p in sorted_content %}
  {% if p.title and p.permalink != '/' and p.permalink != '/archivio/' and p.permalink != '/hub-lingue/' %}
    {% if p.categories == nil or p.categories.size == 0 %}
      <li style="margin-bottom: 10px;">
        <strong><a href="{{ p.url | relative_url }}">{{ p.title }}</a></strong>
        {% if p.subtitle %}<br><small style="color: #666;">{{ p.subtitle }}</small>{% endif %}
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

---

<h2 id="inglese">🇬🇧 Archivio Inglese</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px;">
  <div>
    <h4>Da zero & Pronuncia</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_content %}
      {% if p.url contains '/inglese/da-zero/' or p.url contains '/inglese/pronuncia/' %}
        <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
      {% endif %}
    {% endfor %}
    </ul>
  </div>

  <div>
    <h4>Vocabolario & Frasi</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_content %}
      {% if p.url contains '/inglese/vocabolario/' or p.url contains '/inglese/frasi/' %}
        <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
      {% endif %}
    {% endfor %}
    </ul>
  </div>

  <div>
    <h4>Grammatica & Errori</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_content %}
      {% if p.url contains '/inglese/grammatica/' or p.url contains '/inglese/errori/' %}
        <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
      {% endif %}
    {% endfor %}
    </ul>
  </div>

  <div>
    <h4>Business & Viaggio</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_content %}
      {% if p.url contains '/inglese/business/' or p.url contains '/inglese/viaggio/' %}
        <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
      {% endif %}
    {% endfor %}
    </ul>
  </div>
</div>

<p style="margin-top: 12px;">
  <a href="{{ '/inglese/' | relative_url }}"><strong>Vai all’hub completo di Inglese →</strong></a>
</p>

---

<h2 id="francese">🇫🇷 Archivio Francese</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px;">
  <div>
    <h4>Vocabolario & Frasi</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_content %}
      {% if p.categories contains 'francese' %}
        {% if p.categories contains 'vocabolario' or p.categories contains 'frasi' %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endfor %}
    </ul>
  </div>

  <div>
    <h4>Grammatica & Errori</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_content %}
      {% if p.categories contains 'francese' %}
        {% if p.categories contains 'grammatica' or p.categories contains 'errori' %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endfor %}
    </ul>
  </div>
</div>

---

<h2 id="altre-lingue">🇪🇸 Spagnolo · 🇩🇪 Tedesco · 🇧🇷 Portoghese</h2>
<p>Scopri tutte le altre risorse disponibili nel nostro archivio.</p>

<ul>
{% for p in sorted_content %}
  {% if p.categories %}
    {% if p.categories contains 'spagnolo' or p.categories contains 'tedesco' or p.categories contains 'portoghese' %}
      <li style="margin-bottom: 8px;">
        <span style="font-size: 0.8em; background: #eee; padding: 2px 5px; border-radius: 3px; text-transform: uppercase;">
          {{ p.categories[0] }}
        </span>
        <strong><a href="{{ p.url | relative_url }}">{{ p.title }}</a></strong>
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>
