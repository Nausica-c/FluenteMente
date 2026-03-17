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
  {% assign a1_lessons = site.pages | where: "level", "a1" | sort: "lesson" %}
  {% for lesson in a1_lessons %}
  <div class="lesson-card" style="border-left: 4px solid #007bff; padding: 10px 15px; margin-bottom: 15px; background: #fdfdfd; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
    <h3 style="margin-top: 0; margin-bottom: 5px;">
      <a href="{{ site.baseurl }}{{ lesson.url }}" style="text-decoration: none; color: #333;">
        Lezione {{ lesson.lesson }}: {{ lesson.title }}
      </a>
    </h3>
    <p style="margin: 0; color: #666; font-size: 0.9em;">{{ lesson.subtitle }}</p>
  </div>
  {% endfor %}
</div>

---

{% include bridge-box.html type="base" %}

## 💡 Come usare questo corso al meglio
1. **Costanza:** Dedica 10-15 minuti al giorno. È molto meglio studiare poco ma tutti i giorni, piuttosto che due ore la domenica.
2. **Pronuncia ad alta voce:** Non limitarti a leggere. Ripeti gli esempi ad alta voce per abituare la bocca ai nuovi suoni.
3. **Mettiti alla prova:** Prova a cambiare una parola negli esempi che ti forniamo per creare frasi che parlano della *tua* vita reale.
