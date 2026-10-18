# Struttura repository FluenteMente — versione integrata

## Principio architetturale

La base grafica allegata è stata applicata come livello visuale alla struttura editoriale della Fase 3. I contenuti esistenti, i permalink reali, i 30 record Pinterest e il modulo di approfondimento del funnel sono conservati. La homepage e il sistema grafico sono quelli della base pulita; menu e footer sono stati ricollegati alle pagine realmente presenti.

## Cartelle principali

- `_config.yml`: configurazione Jekyll, URL GitHub Pages, plugin e `launch_mode: true`.
- `_data/pinterest_funnel.yml`: fonte Jekyll per i dati dei Pin e i collegamenti contestuali.
- `_includes/`: header/footer grafici, meta SEO, disclosure affiliata, CTA e modulo di approfondimento.
- `_layouts/`: layout comuni per homepage, pagine, articoli e curiosità.
- `assets/css/main.css`: sistema grafico integrato; mantiene palette blu navy/arancione e componenti responsive.
- `assets/img/`: immagine Open Graph del brand.
- `pages/`: pagine editoriali per hub, beginner, curiosità, grammatica, speaking, viaggio, Business English e Babbel.
- `docs/pinterest/30-pin-publishing.csv`: tracker operativo dei 30 Pin, con UTM e destinazioni.
- `docs/pinterest/fase-3-funnel.md`: note tecniche del funnel.
- `docs/editorial/`: brief editoriali e mappa di riconciliazione, esclusi dalla build pubblica.
- `_archive/`: materiale storico conservato fuori dalla navigazione e dalla pubblicazione ordinaria.

## Modalità di lancio

Il sito rimane in modalità preparazione (`launch_mode: true`). Tutte le pagine hanno quindi `noindex, nofollow` via meta robots. Per una pubblicazione indicizzabile, dopo audit editoriale e legale, impostare `launch_mode: false` e controllare la build con GitHub Actions.

## Analytics e privacy

Gli script Analytics legacy sono stati deliberatamente rimossi dall'head, come previsto dalla base grafica. Prima di attivare GA4 o altri strumenti, configurare la piattaforma di consenso e aggiornare privacy/cookie policy in funzione degli strumenti effettivamente utilizzati. Il CSV mantiene gli UTM ma non implica che Analytics sia attivo.

## Nota sul repository GitHub

Questo ZIP è un pacchetto locale pronto da verificare/caricare. Non modifica automaticamente il repository remoto `Nausica-c/FluenteMente`.
