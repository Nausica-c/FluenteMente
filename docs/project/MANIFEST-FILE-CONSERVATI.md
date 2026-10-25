# Manifest della base grafica e delle integrazioni

## Base grafica conservata

- `_config.yml`
- `_includes/affiliate-disclosure.html`
- `_includes/babbel-next-step.html` e `_includes/babbel-offer.html`
- `_includes/footer.html`, `_includes/head.html`, `_includes/header.html`
- `_layouts/curiosita.html`, `_layouts/default.html`, `_layouts/page.html`, `_layouts/post.html`
- `assets/css/` — fogli di stile e componenti CSS
- `assets/img/og-default.jpg`

## Contenuti attivi

- `index.md`: unica sorgente canonica della home.
- `articoli/`: le 30 versioni più recenti e canoniche della rubrica Pinterest «Lo sapevi che…?».
- `percorsi/hub-c2.md` … `percorsi/hub-c5.md`: quattro hub tematici SEO attivi.
- `pages/servizi/chi-siamo.md`, `pages/servizi/privacy.md`, `pages/servizi/cookie.md`, `pages/servizi/disclaimer.md`: pagine di servizio, da completare/verificare prima del lancio definitivo.
- `manifest_articoli.csv`, `mappa_collegamenti_interni.csv`: inventario e mappa dei collegamenti, aggiornati ai nuovi percorsi sorgente.
- `docs/pinterest-lo-sapevi-che/`: mappe, audit e checklist editoriali.

## Versioni precedenti

- `_archive/legacy-articles/articoli-pre-consolidamento/`: copia integrale della vecchia cartella `articoli/`, conservata senza eliminare file con nomi incompleti o contenuti aggiuntivi. Non è pubblicata.
- `percorsi/`: copie degli hub precedenti, escluse dalla build.

## Indicizzazione e deploy

L'indicizzazione editoriale è abilitata tramite `launch_mode: false`. Le pagine di servizio mantengono esclusioni specifiche fino al completamento dei dati e delle verifiche. Prima del rilascio eseguire la build GitHub Actions e controllare gli URL pubblici generati.

Il pacchetto ZIP non aggiorna automaticamente il repository remoto GitHub.
