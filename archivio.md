---
layout: page
title: "Archivio completo degli articoli"
subtitle: "Tutte le nostre guide, le recensioni e i trucchi per imparare le lingue."
description: "Esplora l'archivio completo di FluenteMente. Trova tutte le guide su inglese, spagnolo, francese e recensioni delle migliori app."
permalink: /archivio/
---

Benvenuto nella libreria completa di **FluenteMente**. Qui trovi ogni singola lezione e analisi pubblicata sul sito, organizzata per lingua e argomento per facilitarti la ricerca.

### Esplora per categoria:
[**Metodo e App**](#metodo) | [**🇬🇧 Inglese**](#inglese) | [**🇫🇷 Francese**](#francese) | [**🇪🇸 Spagnolo**](#spagnolo) | [**🇩🇪 Tedesco**](#tedesco) | [**🇧🇷 Portoghese**](#portoghese)

---

<h2 id="metodo">🚀 Metodo di Studio e Recensioni App</h2>
<p>Le guide fondamentali per approcciare qualsiasi lingua e le nostre analisi oneste sugli strumenti digitali.</p>

<ul>
{% assign sorted_pages = site.pages | sort: "title" %}
{% for p in sorted_pages %}
  {% if p.categories == nil or p.categories.size == 0 %}
    {% if p.title and p.permalink != '/' and p.permalink != '/archivio/' and p.permalink != '/hub-lingue/' %}
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
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
  <div>
    <h4>Vocabolario & Frasi</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_pages %}
      {% if p.categories %}
        {% if p.categories contains 'inglese' and p.categories contains 'vocabolario' or p.categories contains 'frasi' %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endfor %}
    </ul>
  </div>
  <div>
    <h4>Grammatica & Errori</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_pages %}
      {% if p.categories %}
        {% if p.categories contains 'inglese' and p.categories contains 'grammatica' or p.categories contains 'errori' %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endfor %}
    </ul>
  </div>
</div>

---

<h2 id="francese">🇫🇷 Archivio Francese</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
  <div>
    <h4>Vocabolario & Frasi</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_pages %}
      {% if p.categories %}
        {% if p.categories contains 'francese' and p.categories contains 'vocabolario' or p.categories contains 'frasi' %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endfor %}
    </ul>
  </div>
  <div>
    <h4>Grammatica & Errori</h4>
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in sorted_pages %}
      {% if p.categories %}
        {% if p.categories contains 'francese' and p.categories contains 'grammatica' or p.categories contains 'errori' %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endfor %}
    </ul>
  </div>
</div>

---

<h2 id="spagnolo">🇪🇸 Spagnolo, 🇩🇪 Tedesco, 🇧🇷 Portoghese</h2>
<p>Scopri tutte le altre risorse disponibili nel nostro database.</p>

<ul>
{% for p in sorted_pages %}
  {% if p.categories %}
    {% if p.categories contains 'spagnolo' or p.categories contains 'tedesco' or p.categories contains 'portoghese' %}
      <li style="margin-bottom: 8px;">
        <span style="font-size: 0.8em; background: #eee; padding: 2px 5px; border-radius: 3px; text-transform: uppercase;">{{ p.categories[0] }}</span> 
        <strong><a href="{{ p.url | relative_url }}">{{ p.title }}</a></strong>
      </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

---

<div class="cta-soft-box" style="margin-top: 40px; padding: 30px; background: #f9f9f9; border-left: 5px solid #ff7a59; border-radius: 8px;">
<h3>🎯 Trasforma la teoria in pratica</h3>
<p>Hai trovato l'articolo che cercavi? Ottimo. Ora però serve la costanza. Inizia oggi stesso a praticare con il metodo che consigliamo a tutti i nostri lettori adulti.</p>
<a class="btn-primary" href="https://www.awin1.com/awclick.php?gid=322314&mid=9659&awinaffid=2764918&linkid=2038222&clickref=" target="_blank" rel="sponsored nofollow" style="display: inline-block; background: #ff7a59; color: white; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 10px;">
Inizia la tua prova gratuita →
</a>
</div>
