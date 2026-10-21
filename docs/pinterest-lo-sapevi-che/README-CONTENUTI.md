# FluenteMente — home page e 31 articoli Pinterest

Questo pacchetto integra la nuova home page e 31 articoli in Markdown nella base grafica Jekyll fornita, preservando layout, include, fogli di stile e configurazione esistenti.

## Contenuti aggiunti

- `index.md`: home page riscritta, con permalink `/`.
- `articoli/`: 31 articoli con permalink esplicito, ID Pin e metadati SEO.
- `docs/pinterest-lo-sapevi-che/manifest_articoli.csv`: mappa ID Pin / file / permalink / keyword, con cluster SEO e articoli collegati.
- `docs/pinterest-lo-sapevi-che/mappa_cluster_SEO.md`: divisione dei 31 articoli in sei cluster e indicazioni per la struttura hub-and-spoke.
- `docs/pinterest-lo-sapevi-che/controlli_pre-pubblicazione.md`: lista dei controlli finali.

## Note importanti

1. Gli slug sono quelli proposti nei documenti editoriali forniti; non sono stati verificati contro una sitemap o un repository completo di contenuti pubblicati.
2. Non è stata eseguita ricerca web esterna. Gli esempi linguistici devono ricevere una revisione finale e le definizioni più delicate vanno controllate con dizionari affidabili prima della pubblicazione.
3. L’articolo su Babbel non presenta prezzi, sconti, prove, funzioni o condizioni come fatti correnti non verificati. Inserire un link affiliato soltanto dopo averlo verificato e mantenere l’informativa vicino al collegamento.
4. La base grafica contiene link di menu verso pagine/hub che non appartengono a questo piano di 31 Pin; non sono stati inventati contenuti aggiuntivi per tali pagine. Prima della pubblicazione occorre creare queste destinazioni o aggiornare il menu.
5. Il file `_config.yml` originale è stato preservato, incluso `launch_mode: true`. Non disattivare il noindex fino alla verifica finale di contenuti, pagine di servizio, privacy/cookie, analytics e link affiliati.

## Pagine di servizio aggiunte

- `chi-siamo.md`: missione editoriale e principi di FluenteMente.
- `privacy.md`: bozza di informativa sui dati personali, hosting GitHub Pages, diritti e destinatari.
- `cookie.md`: informativa provvisoria basata sull'ispezione statica del repository; non è un inventario certificato dei cookie online.
- `disclaimer.md`: pagina Affiliazioni e trasparenza editoriale, all'indirizzo `/disclaimer/` già usato dal footer e dal componente disclosure.

**Blocco alla pubblicazione:** completare i campi tra parentesi quadre nelle pagine di servizio; verificare il titolare e i recapiti, il comportamento effettivo dei cookie sulla versione online e i link affiliati attivi. Non rimuovere `launch_mode: true` fino al completamento di questi controlli.

Il layout delle pagine e degli articoli non mostra più automaticamente un avviso affiliato su ogni contenuto. L'include può essere attivato tramite `show_affiliate_disclosure: true` nel front matter; la disclosure va comunque resa visibile vicino a ogni effettivo link affiliato.

## Conteggio

32 pagine di contenuto: 1 home page + 31 articoli (`pin01`–`pin31`). I 31 articoli sono stati assegnati a sei cluster principali: C1 (7), C2 (5), C3 (5), C4 (6), C5 (6), C6 (2).

## Collegamenti interni e hub

- I quattro hub C2–C5 sono nei file `../..` del sito: `percorsi/hub-c2.md`, `percorsi/hub-c3.md`, `percorsi/hub-c4.md`, `percorsi/hub-c5.md`.
- La mappa pagina per pagina è in `mappa_collegamenti_interni.csv`.
- L’audit statico e le questioni ancora aperte sono in `audit_collegamenti_interni.md`.
