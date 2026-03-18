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

{% comment %} 
Creiamo una variabile globale sicura che esclude tutte le pagine senza categoria (come la home o l'archivio stesso), evitando il crash di Jekyll.
{% endcomment %}
{% assign pagine_con_cat = site.pages | where_exp: "item", "item.categories != nil" %}

<h2 id="metodo">🚀 Metodo di Studio e Recensioni App</h2>
<p>Le guide fondamentali per approcciare qualsiasi lingua e le nostre analisi oneste sugli strumenti digitali.</p>

<ul>
{% assign generali = site.pages | where_exp: "item", "item.categories == nil" | sort: "title" %}
{% for p in generali %}
  {% if p.title and p.permalink != '/' and p.permalink != '/archivio/' and p.permalink != '/hub-lingue/' %}
    <li style="margin-bottom: 10px;">
      <strong><a href="{{ p.url | relative_url }}">{{ p.title }}</a></strong>
      {% if p.subtitle %}<br><small style="color: #666;">{{ p.subtitle }}</small>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

---

<h2 id="inglese">🇬🇧 Archivio Inglese</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
  <div>
    <h4>Vocabolario & Frasi</h4>
    {% assign ing_voc = pagine_con_cat | where_exp: "item", "item.categories contains 'inglese'" | where_exp: "item", "item.categories contains 'vocabolario' or item.categories contains 'frasi'" | sort: "title" %}
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in ing_voc %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>{% endfor %}
    </ul>
  </div>
  <div>
    <h4>Grammatica & Errori</h4>
    {% assign ing_gramm = pagine_con_cat | where_exp: "item", "item.categories contains 'inglese'" | where_exp: "item", "item.categories contains 'grammatica' or item.categories contains 'errori'" | sort: "title" %}
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in ing_gramm %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>{% endfor %}
    </ul>
  </div>
</div>

---

<h2 id="francese">🇫🇷 Archivio Francese</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
  <div>
    <h4>Vocabolario & Frasi</h4>
    {% assign fra_voc = pagine_con_cat | where_exp: "item", "item.categories contains 'francese'" | where_exp: "item", "item.categories contains 'vocabolario' or item.categories contains 'frasi'" | sort: "title" %}
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in fra_voc %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>{% endfor %}
    </ul>
  </div>
  <div>
    <h4>Grammatica & Errori</h4>
    {% assign fra_gramm = pagine_con_cat | where_exp: "item", "item.categories contains 'francese'" | where_exp: "item", "item.categories contains 'grammatica' or item.categories contains 'errori'" | sort: "title" %}
    <ul style="font-size: 0.9em; padding-left: 20px;">
    {% for p in fra_gramm %}<li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>{% endfor %}
    </ul>
  </div>
</div>

---

<h2 id="spagnolo">🇪🇸 Spagnolo, 🇩🇪 Tedesco, 🇧🇷 Portoghese</h2>
<p>Scopri tutte le altre risorse disponibili nel nostro database.</p>

<ul>
{% assign altre_lingue = pagine_con_cat | where_exp: "item", "item.categories contains 'spagnolo' or item.categories contains 'tedesco' or item.categories contains 'portoghese'" | sort: "title" %}
{% for p in altre_lingue %}
  <li style="margin-bottom: 8px;">
    <span style="font-size: 0.8em; background: #eee; padding: 2px 5px; border-radius: 3px; text-transform: uppercase;">{{ p.categories[0] }}</span> 
    <strong><a href="{{ p.url | relative_url }}">{{ p.title }}</a></strong>
  </li>
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
