---
layout: page
title: "Vocabolario Inglese Livello A1: Il Corso Completo"
subtitle: "Impara le parole fondamentali per iniziare a parlare inglese da zero, basato sulla lista Oxford 3000."
permalink: /inglese/vocabolario/a1/
---

Benvenuto nel tuo punto di partenza per imparare l'inglese! Se stai iniziando da zero o vuoi consolidare le tue basi, sei nel posto giusto.

In questo percorso affronteremo il vocabolario del **Livello A1 (Principiante)**. Abbiamo selezionato i termini più utili e frequenti direttamente dalla **Oxford 3000**, la lista ufficiale delle parole più importanti da conoscere in inglese.

Non studierai liste noiose: ogni lezione contiene tabelle rapide, esempi pratici, mini-storie e dialoghi per farti vedere come le parole prendono vita nella realtà.

---

## 🗺️ Il Tuo Percorso di Studio (Livello A1)

Clicca sulle lezioni qui sotto per iniziare. Segui l'ordine numerico per un apprendimento graduale, oppure salta all'argomento che ti interessa di più!

<div class="lesson-hub" style="margin-top: 20px;">
  {% comment %} 
  SCUDO DI SICUREZZA:
  1. Prendiamo solo le pagine che hanno il campo 'level'
  2. Filtriamo per il livello 'a1'
  3. Ordiniamo per il numero della lezione
  {% endcomment %}
  {% assign level_pages = site.pages | where_exp: "item", "item.level != nil" %}
  {% assign a1_lessons = level_pages | where: "level", "a1" | sort: "lesson" %}
  
  {% for lesson in a1_lessons %}
  <div class="lesson-card" style="border-left: 4px solid #007bff; padding: 15px; margin-bottom: 15px; background: #fdfdfd; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
    <h3 style="margin-top: 0; margin-bottom: 5px; font-size: 1.2em;">
      <a href="{{ lesson.url | relative_url }}" style="text-decoration: none; color: #007bff; font-weight: bold;">
        Lezione {{ lesson.lesson }}: {{ lesson.title }}
      </a>
    </h3>
    {% if lesson.subtitle %}
    <p style="margin: 0; color: #666; font-size: 0.95em;">{{ lesson.subtitle }}</p>
    {% endif %}
  </div>
  {% else %}
    <p><em>Le lezioni del livello A1 sono in fase di caricamento. Torna a trovarci presto!</em></p>
  {% endfor %}
</div>

---

{% include bridge-box.html type="base" %}

## 💡 Come usare questo corso al meglio
1. **Costanza:** Dedica 10-15 minuti al giorno. È molto meglio studiare poco ma tutti i giorni, piuttosto che due ore la domenica.
2. **Pronuncia ad alta voce:** Non limitarti a leggere. Ripeti gli esempi ad alta voce per abituare la bocca ai nuovi suoni.
3. **Mettiti alla prova:** Prova a cambiare una parola negli esempi che ti forniamo per creare frasi che parlano della *tua* vita reale.
