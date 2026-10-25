# FluenteMente — struttura e sorgenti canoniche

## Sorgenti attive

- `index.md`: homepage canonica (`/`).
- `articoli/`: 30 articoli principali PIN01–PIN30, l’articolo conversazionale PIN32 e i contenuti grammaticali supplementari PIN33–PIN34.
- `percorsi/hub-c2.md` … `percorsi/hub-c5.md`: quattro hub SEO attivi; l’hub C2 include PIN32 e l’hub C5 include PIN33 e PIN34.
- `pages/servizi/`: pagine Chi siamo, Privacy, Cookie e Affiliazioni, con permalink invariati e `noindex, follow` finché i dati e i controlli non sono completati.
- `_includes/`, `_layouts/`, `assets/`: componenti e risorse grafiche canoniche.
- `google37d5be4e95f838cc.html`: file di verifica Google mantenuto alla radice del progetto GitHub Pages.

## Archivio

- `_archive/legacy-articles/articoli-pre-consolidamento/`: vecchie versioni dei PIN e file editoriali accessori.
- `_archive/legacy-structure/`: copie root duplicate di template/CSS/immagini, precedenti copie degli hub, documenti storici e piccoli artefatti anomali conservati per tracciabilità. L'intera cartella è esclusa dalla build.

## Documentazione

- `docs/marketing/`: decisioni e note sul funnel Babbel.
- `docs/pinterest-lo-sapevi-che/`: manifest, mappa SEO, collegamenti interni, audit e checklist pre-pubblicazione.
- `docs/project/`: documentazione di struttura, indicizzazione e manifest del pacchetto.

## Principi di manutenzione

1. Ogni articolo o pagina deve avere una sola sorgente attiva e un solo permalink.
2. Non ripristinare i file d'archivio nella build senza revisione.
3. I CSS pubblici sono collegati da `_includes/head.html` (`/assets/css/main.css`). I CSS componenti restano organizzati in `assets/css/components/`; i file legacy alla radice sono archiviati.
4. `launch_mode: false` consente di rendere indicizzabili i contenuti editoriali. Le pagine di servizio restano non indicizzabili finché non vengono completati titolare, recapiti e controlli tecnici.
5. Prima del rilascio eseguire la build Jekyll tramite GitHub Actions e verificare link, canonical, sitemap, meta robots e link Awin. Lo ZIP locale non aggiorna il repository remoto.
