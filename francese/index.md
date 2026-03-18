---
layout: page
title: "Imparare il Francese: Il percorso completo per adulti"
subtitle: "Da livello zero fino alla conversazione fluida. Scopri grammatica, pronuncia, francese per il lavoro e per viaggiare."
description: "L'hub definitivo per imparare il francese da adulti. Risorse su grammatica, vocabolario, francese per il lavoro, viaggi, pronuncia ed errori comuni."
permalink: /francese/
---

Il francese è la lingua dell'eleganza, della diplomazia, dell'arte e della gastronomia. Che ti serva per passeggiare a Parigi, per espandere il tuo business o semplicemente per piacere personale, sei nel posto giusto.

Se ti senti bloccato, se la pronuncia ti spaventa o se semplicemente non sai da che parte iniziare, questa è la tua mappa. Abbiamo diviso le nostre migliori guide in categorie: parti da zero, perfeziona i suoni, arricchisci il vocabolario e inizia finalmente a pensare in francese.

{% include promo-box.html type="base" lang="francese" %}

---

{% comment %} 
Filtro di sicurezza a monte: prendiamo solo le pagine che hanno la voce "category" compilata, 
e filtriamo subito solo quelle che contengono "francese" per non far crashare Liquid.
{% endcomment %}
{% assign safe_pages = site.pages | where_exp: "item", "item.categories != nil" %}
{% assign french_pages = safe_pages | where_exp: "item", "item.categories contains 'francese'" %}

## 1. Da dove iniziare (Mindset e Livello Zero)

{% assign da_zero_pages = french_pages | where_exp: "item", "item.categories contains 'da-zero'" %}
<ul>
{% for item in da_zero_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if da_zero_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/da-zero/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ da_zero_pages.size }} articoli su come iniziare ➔</a></div>
{% endif %}

---

## 2. Risolvi il problema della Pronuncia

{% assign pronuncia_pages = french_pages | where_exp: "item", "item.categories contains 'pronuncia'" %}
<ul>
{% for item in pronuncia_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if pronuncia_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/pronuncia/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ pronuncia_pages.size }} articoli sulla pronuncia ➔</a></div>
{% endif %}

---

## 3. Grammatica (Senza mal di testa)

{% assign grammatica_pages = french_pages | where_exp: "item", "item.categories contains 'grammatica'" %}
<ul>
{% for item in grammatica_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if grammatica_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/grammatica/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ grammatica_pages.size }} articoli di grammatica ➔</a></div>
{% endif %}

{% include promo-box.html type="grammatica" lang="francese" %}

---

## 4. Vocabolario: Le parole che servono davvero

{% assign vocabolario_pages = french_pages | where_exp: "item", "item.categories contains 'vocabolario'" %}
<ul>
{% for item in vocabolario_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if vocabolario_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/vocabolario/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ vocabolario_pages.size }} articoli di vocabolario ➔</a></div>
{% endif %}

{% include promo-box.html type="vocabolario" lang="francese" %}

---

## 5. Gli Errori Tipici e i "Faux Amis"

{% assign errori_pages = french_pages | where_exp: "item", "item.categories contains 'errori'" %}
<ul>
{% for item in errori_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if errori_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/errori/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ errori_pages.size }} articoli sugli errori ➔</a></div>
{% endif %}

{% include promo-box.html type="errori" lang="francese" %}

---

## 6. Frasi ed Espressioni di Vita Reale

{% assign frasi_pages = french_pages | where_exp: "item", "item.categories contains 'frasi'" %}
<ul>
{% for item in frasi_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if frasi_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/frasi/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ frasi_pages.size }} articoli sulle frasi utili ➔</a></div>
{% endif %}

---

## 7. Curiosità, Idiomi e Cultura

{% assign curiosita_pages = french_pages | where_exp: "item", "item.categories contains 'curiosita'" %}
<ul>
{% for item in curiosita_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if curiosita_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/curiosita/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ curiosita_pages.size }} articoli su curiosità e idiomi ➔</a></div>
{% endif %}

---

## 8. Francese per il Lavoro

{% assign business_pages = french_pages | where_exp: "item", "item.categories contains 'business'" %}
<ul>
{% for item in business_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if business_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/business/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ business_pages.size }} articoli per il lavoro ➔</a></div>
{% endif %}

{% include promo-box.html type="business" lang="francese" %}

---

## 9. Francese in Viaggio: Sopravvivere all'estero

{% assign viaggio_pages = french_pages | where_exp: "item", "item.categories contains 'viaggio'" %}
<ul>
{% for item in viaggio_pages limit: 10 %}
  <li style="margin-bottom: 15px;">👉 <strong><a href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
    <br><small style="color: #555;">{% if item.description %}{{ item.description }}{% else %}{{ item.excerpt | strip_html | truncatewords: 25 }}{% endif %}</small>
  </li>
{% else %}
  <li><em>Nuovi articoli in arrivo a breve!</em></li>
{% endfor %}
</ul>

{% if viaggio_pages.size > 10 %}
  <div style="text-align: right; margin-bottom: 20px;"><a href="{{ '/francese/viaggio/' | relative_url }}" style="font-weight: bold; color: #0056b3; text-decoration: none;">Vedi tutti i {{ viaggio_pages.size }} articoli per viaggiare ➔</a></div>
{% endif %}

{% include promo-box.html type="viaggio" lang="francese" %}

---

<div class="cta-soft-box" style="margin-top: 30px; padding: 20px; background: #eef5fa; border-radius: 8px; text-align: center;">
  <h3 style="margin-top: 0;">🎯 Trasforma la teoria in pratica</h3>
  <p>Leggere gli articoli è utile, ma per imparare a parlare devi allenarti ogni giorno. Scopri l'app che consigliamo agli adulti per imparare il francese in modo strutturato.</p>
  <a class="btn-primary" href="{{ '/recensione-babbel/' | relative_url }}" style="display: inline-block; padding: 12px 24px; background: #0056b3; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
    Leggi la nostra recensione e il metodo consigliato
  </a>
</div>
