# FluenteMente — base grafica integrata

Questo repository conserva la base grafica Jekyll originale e la integra con la nuova architettura editoriale. I CSS, i layout e gli include principali sono mantenuti.

## Struttura inclusa

- `_config.yml`: configurazione del sito; `launch_mode: false` abilita l’indicizzazione dei contenuti editoriali. Le pagine di servizio incomplete mantengono un noindex specifico.
- `_layouts/` e `_includes/`: struttura grafica condivisa e navigazione.
- `assets/css/` e `assets/img/`: fogli di stile e immagine social.
- `index.md`: unica sorgente canonica della nuova home page, ottimizzata per mobile; eliminare dal repository online il vecchio `index.html` in radice prima del rilascio. Il CSS della home è isolato tramite `home-page`.
- `articoli/`: i 30 articoli Pinterest, con permalink espliciti e metadati.
- `percorsi/`: quattro hub tematici SEO.
- `pages/servizi/chi-siamo.md`, `pages/servizi/privacy.md`, `pages/servizi/cookie.md`, `pages/servizi/disclaimer.md`: pagine di servizio.
- `docs/pinterest-lo-sapevi-che/`: mappe, manifest e checklist di controllo.

## Prima della pubblicazione

La privacy e la cookie policy sono bozze preparate sulla base della configurazione visibile nel repository. L'indicizzazione dei contenuti editoriali è attiva tramite `launch_mode: false`; Privacy, Cookie, Chi siamo e Affiliazioni restano temporaneamente `noindex, follow` ed escluse dalla sitemap finché non vengono completati i campi reali e le verifiche richieste. Prima del deploy definitivo, completare la checklist in `docs/pinterest-lo-sapevi-che/controlli_pre-pubblicazione.md` e validare la build Jekyll su GitHub Actions.

Leggi `docs/pinterest-lo-sapevi-che/CONSOLIDAMENTO-HOME.md` prima di copiare la modifica sul repository GitHub: indica la rimozione del vecchio `index.html` e i controlli di rilascio.
