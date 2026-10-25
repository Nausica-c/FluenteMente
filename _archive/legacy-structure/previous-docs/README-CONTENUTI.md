# FluenteMente — home page e 30 articoli Pinterest

Documento di riferimento per la struttura dei contenuti, le sorgenti canoniche e i controlli di pubblicazione di FluenteMente.

## Sorgenti editoriali attive

- `index.md`: home page con permalink `/`.
- `articoli/`: contiene le 30 versioni editoriali più recenti e canoniche dei PIN01–PIN30. Ogni articolo mantiene il proprio permalink; il percorso del file sorgente non cambia l'URL pubblico.
- `hub-c2.md` … `hub-c5.md`: sorgenti canoniche dei quattro hub tematici attivi nella radice.
- `manifest_articoli.csv` e `mappa_collegamenti_interni.csv`: inventario, destinazioni e collegamenti editoriali, con percorsi sorgente aggiornati.
- `docs/pinterest-lo-sapevi-che/`: materiali di lavoro, mappa cluster e controlli pre-pubblicazione; esclusi dall'output pubblico.

## Versioni precedenti conservate

- `_archive/legacy-articles/articoli-pre-consolidamento/`: copia integrale dei file che si trovavano prima in `articoli/`, inclusi le versioni precedenti, i file orfani e quelli con nomi incompleti. Sono conservati per confronto e recupero, ma non partecipano alla build Jekyll.
- `percorsi/`: copie storiche degli hub, escluse dalla build; le sorgenti attive degli hub sono `hub-c2.md` … `hub-c5.md` nella radice.
- I file HTML legacy nella radice (`head.html`, `header.html`, `footer.html`, `default.html`, `page.html`, `post.html`, `curiosita.html` e i frammenti affiliati) sono esclusi: le versioni attive sono in `_includes/` e `_layouts/`.

## Note importanti

1. I permalinks degli articoli sono stati mantenuti invariati durante lo spostamento. È presente una sola sorgente attiva per ogni PIN.
2. Eseguire comunque una build Jekyll su GitHub Actions prima del rilascio e verificare la sitemap e i link interni nel sito generato.
3. Le caratteristiche di Babbel, i prezzi, le promozioni e le condizioni possono cambiare: consultare le fonti ufficiali collegate nella guida prima di aggiornare affermazioni commerciali.
4. Il file `_config.yml` usa `launch_mode: false`: i contenuti editoriali sono predisposti per l'indicizzazione. Le pagine `privacy.md`, `cookie.md`, `chi-siamo.md` e `disclaimer.md` restano temporaneamente `noindex, follow` ed escluse dalla sitemap finché dati e controlli non sono completati.
5. Prima del deploy definitivo, completare i recapiti delle pagine di servizio e controllare build Jekyll, canonical, meta robots e link Awin.

## Audit Babbel

Il rapporto aggiornato è in `audit_babbel_articoli_30.md`. Le CTA soft verso Babbel sono selettive e la CTA affiliata diretta resta nella guida PIN27.
