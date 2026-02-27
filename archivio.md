---
layout: page
title: "Archivio completo degli articoli"
subtitle: "Tutte le nostre guide, le recensioni e i trucchi per imparare le lingue, dal più recente al più vecchio."
description: "Esplora l'archivio completo di FluenteMente. Trova tutte le guide su inglese, spagnolo, metodo di studio e recensioni delle app."
permalink: /archivio/
---

Benvenuto nella libreria completa di **FluenteMente**. 

Qui trovi tutti gli articoli, le guide grammaticali, le analisi sui falsi amici e le recensioni che abbiamo pubblicato nel corso del tempo. Se stai cercando qualcosa di specifico per la lingua che stai studiando, ti consigliamo di visitare prima i nostri **[Hub dedicati]({{ '/hub-lingue/' | relative_url }})**.

Se invece vuoi curiosare tra le nostre ultime pubblicazioni, ecco l'elenco completo in ordine cronologico.

---

## Tutti gli articoli pubblicati

{% for post in site.posts %}
  {% capture current_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% if current_year != previous_year %}
    {% unless forloop.first %}
      </ul>
    {% endunless %}
    <h3 style="margin-top: 30px; border-bottom: 2px solid var(--text-light); padding-bottom: 5px;">{{ current_year }}</h3>
    <ul style="list-style-type: none; padding-left: 0;">
    {% capture previous_year %}{{ current_year }}{% endcapture %}
  {% endif %}
  
  <li style="margin-bottom: 15px; display: flex; align-items: baseline;">
    <span style="color: var(--text-light); font-size: 0.9em; min-width: 60px; font-family: monospace;">{{ post.date | date: "%d/%m" }}</span>
    <span>
      👉 <strong><a href="{{ post.url | relative_url }}" style="font-size: 1.1em;">{{ post.title }}</a></strong>
      {% if post.subtitle %}<br><span style="font-size: 0.9em; color: var(--text-light);">{{ post.subtitle }}</span>{% endif %}
    </span>
  </li>

  {% if forloop.last %}
    </ul>
  {% endif %}
{% endfor %}

---

<div class="cta-soft-box" style="margin-top: 40px;">
<h3>🎯 Non sai da dove cominciare?</h3>
<p>Troppi articoli da leggere? Inizia dalle basi assolute applicando il nostro metodo con l'app più strutturata per gli adulti.</p>
<a class="btn-primary" href="https://www.awin1.com/awclick.php?gid=322314&mid=9659&awinaffid=2764918&linkid=2038222&clickref=" target="_blank" rel="sponsored nofollow">
Prova la tua prima lezione gratuita
</a>
</div>
