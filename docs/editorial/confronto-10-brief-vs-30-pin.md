# FluenteMente — Confronto tra i 10 brief editoriali e i 30 Pin della Fase 3

**Data analisi:** 17 ottobre 2026  
**Obiettivo:** riconciliare il piano dei primi 10 articoli con i 30 Pin Pinterest della Fase 3, riducendo sovrapposizioni, URL alternativi e ambiguità nella struttura editoriale.

## 1. Sintesi esecutiva

I due piani sono compatibili come strategia, ma **non devono essere pubblicati come due insiemi indipendenti di articoli**. Il piano iniziale dei 10 articoli è centrato su errori linguistici, situazioni di viaggio, metodo di studio, ascolto e due pagine commerciali Babbel. La Fase 3 estende il sito con 30 destinazioni in nove aree e usa i Pin per portare traffico a pagine didattiche già organizzate nel repository.

Il confronto evidenzia:

- **6 corrispondenze dirette o quasi dirette**: errori comuni, falsi amici, aeroporto, ristorante, colloquio di lavoro e present perfect/past simple.
- **3 contenuti da mantenere ma con ruolo distinto**: piano di studio di 30 giorni, guida al listening e confronto Babbel vs Duolingo.
- **1 contenuto commerciale da mantenere come passaggio del funnel**, non come destinazione predefinita di un Pin: recensione Babbel.
- **Un problema di governance degli URL**: i permalink del piano ART001–ART010 sono spesso diversi dalle destinazioni attuali dei Pin, pur rispondendo allo stesso intento. La soluzione è riallineare i brief alle pagine canoniche esistenti, non creare copie con slug alternativi.

### Decisione raccomandata

Usare le destinazioni della Fase 3 come riferimento per le pagine didattiche già collegate ai Pin; aggiornare i brief dei 10 articoli perché diventino specifiche editoriali per le pagine giuste. Mantenere come pagine autonome solo i contenuti con un intento davvero distinto.

---

## 2. Materiali confrontati e limiti

1. **Piano dei primi 10 articoli**: `piano_editoriale_babbel_primi_10_articoli.yml` (ART001–ART010), da cui derivano i brief editoriali per i dieci contenuti.
2. **Piano di pubblicazione**: `FluenteMente-phase3-30-pin-publishing.csv`, con 30 Pin, destinazioni, UTM, articoli correlati e flag di collegamento a Babbel.
3. **Piano funnel**: `FluenteMente-phase3-funnel-plan.md`.
4. **Audit Fase 3**: `FluenteMente-phase3-audit.txt`.

**Nota di precisione:** il confronto analizza il contenuto editoriale del piano ART001–ART010 e lo mette a confronto con il CSV dei 30 Pin della Fase 3. L'archivio ZIP dei dieci brief non è stato ispezionabile direttamente come archivio in questo ambiente; se il contenuto dello ZIP differisce dal piano YAML, le differenze vanno verificate prima di applicare le modifiche proposte.

Il controllo statico della Fase 3 dichiara 30 destinazioni su 30 presenti nel repository e 60 link di approfondimento su 60 verificati. Non dichiara però completata la build Jekyll né eseguito un controllo HTTP su tutte le pagine pubblicate. Nel CSV, lo stato di tutti i 30 Pin è `da creare`.

---

## 3. Matrice di corrispondenza: 10 articoli vs 30 Pin

| Brief iniziale | Pin Fase 3 collegato | Tipo di rapporto | Decisione consigliata |
|---|---|---|---|
| **ART001 — 10 errori comuni in inglese** (`/errori-comuni-inglese-italiani/`) | **LSC002** — 10 errori comuni degli italiani in inglese (`/inglese/errori/errori-comuni-italiani-inglese/`). In relazione anche a LSC001 e a contenuti grammaticali specifici. | **Duplicazione d'intento alta.** Titolo, promessa e parola chiave sono sostanzialmente gli stessi. Il brief ART001 cita inoltre falsi amici, make/do, say/tell, I agree e l'età: una parte di questi argomenti ha o può avere approfondimenti dedicati. | Mantenere una sola pagina canonica: la destinazione corrente di LSC002. Trasferire lì la struttura e gli esempi migliori di ART001. Gli errori devono essere spiegati in sintesi nella guida generale e collegati agli approfondimenti specifici, senza copiarne intere sezioni. Il vecchio URL va valutato come redirect solo se è stato pubblicato o linkato. |
| **ART002 — 15 falsi amici inglese-italiano** (`/falsi-amici-inglese-italiano/`) | **LSC001** — Falsi amici in inglese: la guida per italiani (`/inglese/errori/falsi-amici-inglese-guida/`). | **Corrispondenza diretta.** Stesso bisogno di ricerca; ART002 promette una lista ragionata di 15 parole. | Usare la destinazione LSC001 come URL canonico e incorporare nel relativo brief la tabella dei 15 falsi amici, gli esempi contestuali e il mini-quiz. Non creare una seconda guida generale. LSC002 può collegarsi a questa pagina per approfondire i falsi amici. |
| **ART003 — Inglese in aeroporto: 25 frasi e dialoghi** (`/inglese-aeroporto-frasi-utili/`) | **LSC022** — Inglese in aeroporto: frasi utili (`/inglese/viaggio/inglese-aeroporto-frasi/`). In relazione anche a LSC025, kit generale di viaggio. | **Corrispondenza diretta.** Stesso scenario e intento. Il diverso numero di frasi non giustifica due pagine separate. | Aggiornare il brief ART003 perché descriva la pagina LSC022. Se si mantiene la promessa di 25 frasi, completarli davvero: il piano iniziale contiene solo 14 frasi specificate. Tenere l'aeroporto come pagina specifica e lasciare a LSC025 un kit generale per più situazioni di viaggio, evitando liste copiate. |
| **ART004 — Imparare l'inglese da zero da adulti: piano di 30 giorni** (`/imparare-inglese-da-zero-adulti/`) | Collegamenti tematici: **LSC012** — 5 frasi al giorno; **LSC020** — vocabolario base per adulti; **LSC026** — preparare l'inglese per un viaggio in 7 giorni; **LSC030** — routine di 15 minuti. | **Sovrapposizione parziale, non duplicazione automatica.** Tutti parlano di studio e routine, ma possono rispondere a domande diverse. | Mantenere ART004 come percorso progressivo di 30 giorni per adulti principianti, solo dopo aver controllato che non duplichi una guida già esistente nel repository. LSC030 deve restare una routine giornaliera breve; LSC026 una preparazione mirata a un viaggio; LSC012 un metodo di pratica con cinque frasi. Non trasformare ART004 in un'altra guida generica sui 15 minuti. |
| **ART005 — Babbel per imparare l'inglese: come funziona, vantaggi e limiti** (`/recensione-babbel-inglese/`) | Nessun Pin dei 30 ha la recensione come destinazione primaria. **14 Pin** riportano `bridge_to_babbel = sì`; il funnel prevede il passaggio contestuale alla recensione da una selezione di articoli. | **Ruolo complementare di conversione.** È una pagina commerciale/informativa di supporto al funnel, non una mini-lezione concorrente con le altre. | Mantenere una sola recensione canonica nel sito e verificare il relativo permalink attuale prima di riutilizzare lo slug ART005. Usarla come passaggio intermedio per gli articoli pertinenti; non inserire un collegamento affiliato diretto in ogni pagina. Presentare vantaggi, limiti, destinatari, informazioni verificate e disclosure. |
| **ART006 — Inglese al ristorante: 30 frasi e dialoghi** (`/inglese-al-ristorante-frasi-utili/`) | **LSC021** — Ordinare al ristorante in inglese (`/inglese/viaggio/inglese-al-ristorante/`). Relazione secondaria con LSC025, kit generale da viaggio. | **Corrispondenza diretta.** Stesso scenario e stessa intenzione. | Consolidare il brief ART006 nella pagina LSC021. Se il titolo promette 30 frasi, completarli e aggiungere dialoghi e traduzioni. Il kit da viaggio può raccogliere poche frasi selezionate e rinviare alla guida ristorante per l'approfondimento. |
| **ART007 — Come capire l'inglese parlato: 7 esercizi per migliorare l'ascolto** (`/capire-inglese-parlato/`) | **LSC011** — Tecnica dello shadowing per allenare il parlato (`/inglese/speaking/tecnica-shadowing-inglese/`). In relazione più ampia con LSC006, LSC008 e LSC009. | **Relazione complementare con rischio di sovrapposizione didattica.** Il listening riguarda il riconoscimento e la comprensione; lo shadowing è una tecnica di ripetizione/produzione guidata. | Mantenere le due pagine distinte. ART007 deve concentrarsi su ascolto senza testo, parole chiave, controllo della trascrizione e comprensione globale. LSC011 deve concentrarsi sulla procedura di shadowing e sui suoi limiti. ART007 richiede una risorsa audio utilizzabile e una trascrizione: verificarne disponibilità e diritti prima della pubblicazione. |
| **ART008 — Colloquio di lavoro in inglese: 25 frasi e risposte** (`/colloquio-lavoro-inglese-frasi/`) | **LSC029** — Colloquio di lavoro in inglese: 10 domande e risposte (`/inglese/business/colloquio-di-lavoro-domande/`). In relazione con LSC027, email formali, e LSC028, riunioni/video-call. | **Duplicazione d'intento alta.** I due titoli promettono sostanzialmente la stessa preparazione a un colloquio. Cambiare il numero di frasi non è sufficiente per giustificare due pagine. | Tenere una sola pagina canonica: la destinazione già usata da LSC029. Integrare nel brief corrente domande, risposte personalizzabili, frasi per chiedere chiarimenti e una o due simulazioni. Il brief iniziale elenca 16 formule a fronte delle 25 promesse: completare o rimuovere il numero dal titolo. Non confondere il tema colloquio con email e riunioni, che restano intenti distinti. |
| **ART009 — Present perfect o past simple?** (`/present-perfect-vs-past-simple/`) | **LSC014** — Present Perfect vs Past Simple (`/inglese/grammatica-pratica/present-perfect-vs-past-simple/`). LSC013 tratta invece Present Simple vs Present Continuous. | **Corrispondenza diretta.** L'intento grammaticale e la keyword sono gli stessi; la differenza è nel percorso URL. | Usare la destinazione corrente LSC014 come canonica e trasferire lì spiegazioni, esempi ed esercizi del brief ART009. Il brief resta didatticamente valido; va cambiato il permalink e verificata la presenza dei dieci esercizi con soluzioni. LSC013 rimane separato perché tratta un contrasto grammaticale diverso. |
| **ART010 — Babbel vs Duolingo** (`/babbel-vs-duolingo/`) | Nessun Pin LSC001–LSC030 porta direttamente a questa pagina; la Fase 3 la considera parte del gruppo di pagine commerciali ad alta intenzione, insieme a recensione e guide di valutazione. | **Contenuto distinto e ad alta intenzione commerciale.** Non è duplicato dai Pin didattici. | Mantenerlo come confronto separato, purché basato su criteri espliciti, informazioni aggiornate e limiti per entrambi i prodotti. Collegarlo dalla recensione Babbel e da contenuti ad alta intenzione. Non aggiungere ora un Pin dedicato solo per forza: valutare un Pin comparativo dopo i primi dati organici. Verificare che non esista già una pagina canonica con un diverso slug. |

---

## 4. Le criticità più importanti

### A. URL alternativi per lo stesso contenuto

Le sei coppie con sovrapposizione alta sono ART001/LSC002, ART002/LSC001, ART003/LSC022, ART006/LSC021, ART008/LSC029 e ART009/LSC014. Gli URL proposti dal piano iniziale e gli URL del CSV sono differenti, ma rispondono allo stesso intento. Questo non è necessariamente un conflitto tecnico di permalink nel repository; è un rischio editoriale e SEO se si pubblicano due pagine con contenuto e promessa equivalenti.

**Regola:** per ciascuna coppia mantenere una sola destinazione canonica, scegliere il brief migliore e trasferire nel documento canonico gli elementi utili dell'altro. Se un vecchio URL è già stato pubblicato o collegato dall'esterno, decidere un redirect permanente anziché lasciarlo come seconda pagina concorrente.

### B. Gli articoli “ombrello” devono linkare agli approfondimenti

ART001 contiene in forma introduttiva diversi temi presenti in altri articoli, e tra i Pin Fase 3 ci sono pagine dedicate a falsi amici, grammatica e phrasal verbs. La soluzione non è togliere gli esempi dalla guida generale, ma limitarli a una spiegazione sintetica e collegare gli approfondimenti. Lo stesso vale per il kit generale di viaggio: deve selezionare le frasi più utili, non duplicare intere guide aeroporto e ristorante.

### C. I numeri nei titoli devono corrispondere al contenuto

Nel piano ART003 promette 25 frasi ma specifica 14 frasi iniziali; ART008 promette 25 formule e ne elenca 16. Prima della scrittura finale vanno completate le liste o riformulati i titoli. ART006 deve avere davvero 30 frasi se mantiene quel numero. Ogni cifra usata nel Pin deve essere mantenuta anche dalla pagina di destinazione.

### D. Babbel deve restare un passaggio, non dominare tutto il sito

Nel CSV Fase 3, 14 Pin su 30 hanno il flag `bridge_to_babbel = sì`; il flag va interpretato come ponte editoriale contestuale e non come autorizzazione a inserire una promozione diretta in ogni articolo. Il piano funnel stabilisce un percorso: Pin → pagina che risponde alla promessa → due approfondimenti pertinenti → eventuale recensione Babbel → link affiliato sulle pagine ad alta intenzione. La vendita non deve sostituire il valore didattico.

### E. Brand e URL base

Nel piano YAML dei dieci articoli compare ancora `working_site_name: Inglese in Pratica`, indicato come provvisorio. Per il progetto attuale il brand da usare è **FluenteMente**. Inoltre il piano dei dieci articoli risale a una precedente versione di architettura; il riferimento URL attuale indicato dal file di correzione repository è `https://nausica-c.github.io/FluenteMente/`. Non riutilizzare automaticamente gli slug e i link del vecchio piano senza confrontarli con il repository corrente.

---

## 5. Che cosa dei 10 brief merita di essere conservato

| Brief | Elementi di valore da mantenere nel contenuto canonico |
|---|---|
| ART001 | Struttura ripetibile per ogni errore: forma da evitare, forma corretta, spiegazione, esempi e mini-esercizio; tono non giudicante. |
| ART002 | Tabella mobile-friendly dei 15 falsi amici, dialoghi contestuali e quiz con soluzioni. Controllare con dizionari le sfumature di ciascuna traduzione. |
| ART003 | Suddivisione per check-in, sicurezza, gate/imbarco e bagagli; due dialoghi completi con traduzione. Completare l'inventario fino al numero promesso. |
| ART004 | Percorso progressivo di 30 giorni con attività concrete, evitando la promessa irrealistica di “imparare l'inglese in 30 giorni”. |
| ART005 | Separazione tra fatti verificati, valutazione editoriale, vantaggi, limiti e disclosure; nessun prezzo/offerta non verificato. |
| ART006 | Frasi raggruppate per fase del pasto, richieste cortesi, conto, allergie o problemi; dialoghi brevi e traduzione. Evitare il duplicato del kit generale di viaggio. |
| ART007 | Procedura di ascolto in passi ripetibili, esercizio guidato di cinque minuti e segnali pratici di progresso; reperire audio utilizzabili. |
| ART008 | Modelli di risposta adattabili alla vera esperienza del candidato, domande di chiarimento e simulazioni; non suggerire risposte finte o successo garantito. |
| ART009 | Contrasti basati su contesto e riferimento temporale, esempi paralleli ed esercizi commentati; evitare equivalenze automatiche con i tempi italiani. |
| ART010 | Confronto imparziale basato su criteri espliciti, verifica corrente di funzioni/costi e spiegazione di quale profilo potrebbe preferire ciascuna soluzione. |

---

## 6. Sequenza di lavoro consigliata

1. **Consolidare i sei doppioni d'intento**: aggiornare i brief ART001, ART002, ART003, ART006, ART008 e ART009 usando i permalink della Fase 3 come riferimento. Non creare nuovi file Markdown per i vecchi slug finché non è stata decisa la strategia canonica/redirect.
2. **Verificare ART004** rispetto alla guida da zero, al percorso principianti e alla routine di 15 minuti già presenti nel repository. Tenerlo solo se l'angolo “piano in 30 giorni per adulti” rimane chiaramente distinto.
3. **Separare ART007 e LSC011** nella promessa, nella struttura e negli esempi; verificare la risorsa audio prima di scrivere/pubblicare.
4. **Mantenere ART005 e ART010 nel cluster commerciale**, collegandoli alle pagine didattiche pertinenti ma non trasformandoli in destinazioni predefinite dei 30 Pin.
5. **Allineare il brand**: sostituire “Inglese in Pratica” con FluenteMente nei brief e nei metadati in cui compare il nome provvisorio.
6. **Fare QA prima del rilascio**: permalink, canonical, redirect, link interni, esempi linguistici, conteggi promessi, disclosure affiliata e build GitHub Actions. L'audit statico da solo non prova che tutte le URL UTM funzionino sul sito pubblicato.

---

## 7. Valutazione finale

Il piano dei dieci articoli conserva ottime specifiche didattiche e due pagine commerciali utili, ma non va aggiunto “così com'è” al sito della Fase 3. La Fase 3 contiene già destinazioni più organizzate per categorie e sei temi sono presenti in entrambe le architetture con URL diversi.

La strategia migliore è **consolidare, non moltiplicare**: usare i 30 Pin per sostenere una rete editoriale più ampia; riutilizzare i brief iniziali come materiale di qualità da trasferire sulle pagine canoniche; conservare piano di 30 giorni, listening e confronto Babbel/Duolingo come articoli autonomi solo dopo aver verificato che il loro intento sia distinto e che non esistano già pagine equivalenti nel repository.
