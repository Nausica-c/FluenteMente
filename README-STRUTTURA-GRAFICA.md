# FluenteMente — base grafica integrata

Questo repository conserva la base grafica Jekyll originale e la integra con la nuova architettura editoriale. I CSS, i layout e gli include principali sono mantenuti.

## Struttura inclusa

- `_config.yml`: configurazione del sito; `launch_mode: true` mantiene il sito in modalità noindex.
- `_layouts/` e `_includes/`: struttura grafica condivisa e navigazione.
- `assets/css/` e `assets/img/`: fogli di stile e immagine social.
- `index.md`: unica sorgente canonica della nuova home page; eliminare dal repository online il vecchio `index.html` in radice prima del rilascio.
- `articoli/`: i 30 articoli Pinterest, con permalink espliciti e metadati.
- `percorsi/`: quattro hub tematici SEO.
- `chi-siamo.md`, `privacy.md`, `cookie.md`, `disclaimer.md`: pagine di servizio.
- `docs/pinterest-lo-sapevi-che/`: mappe, manifest e checklist di controllo.

## Prima della pubblicazione

La privacy e la cookie policy sono bozze preparate sulla base della configurazione visibile nel repository. Occorre completare i campi tra parentesi quadre, confermare l'identità e i recapiti del titolare, eseguire un controllo dei cookie sulla versione online, validare i link affiliati e lanciare un build Jekyll. Non disattivare `launch_mode: true` prima di avere completato la checklist in `docs/pinterest-lo-sapevi-che/controlli_pre-pubblicazione.md`.

Leggi `docs/pinterest-lo-sapevi-che/CONSOLIDAMENTO-HOME.md` prima di copiare la modifica sul repository GitHub: indica la rimozione del vecchio `index.html` e i controlli di rilascio.
