# Consolidamento della home page

## Sorgente canonica

La home page del pacchetto consolidato è **`index.md`**, con `permalink: /` e layout Jekyll `page`. È l'unica sorgente della home inclusa nella radice di questo repository. La pagina usa il layout esistente, la configurazione SEO, i CSS condivisi e i componenti CSS dedicati alla home.

## Azione obbligatoria sul repository GitHub esistente

La versione online di partenza conteneva anche un vecchio **`index.html`** nella radice, distinto da `index.md`. L'archivio fornito per questo intervento non conteneva quel file legacy. Prima di copiare i nuovi file nel repository GitHub, **elimina il vecchio file `/index.html` dalla radice** e conserva solo `/index.md`. Non lasciare due file sorgente che tentano di generare la pagina `/`.

Dopo il commit, controlla che la home pubblicata sia quella nuova e non la precedente. Il pacchetto locale non è stato pubblicato direttamente su GitHub.

## Cosa mostra la nuova home

- titolo e sottotitolo compattati su mobile, con maggiore contrasto e meno spazio vuoto sopra il titolo;
- riquadro «Lo sapevi che…?» con testo abbreviato e un solo pulsante principale, «Scopri la prima mini-lezione»;
- primi tre contenuti messi in evidenza (Pin 01, 02 e 03);
- sei percorsi tematici con collegamenti ai rispettivi hub o guide centrali;
- breve spiegazione del percorso didattico;
- sezione finale sui metodi e sugli strumenti, con Babbel come opzione da valutare e non come unica soluzione;
- collegamento alle informazioni sul progetto e sulla trasparenza delle affiliazioni.

## Controlli

- `index.md` è l'unico file della home nella radice del pacchetto;
- i link interni della home sono stati confrontati con i permalink dei contenuti inclusi;
- gli stili aggiunti sono circoscritti alla home tramite la classe `home-page` sul `body`, senza cambiare intenzionalmente la grafica delle pagine articolo;
- il campo `seo_title` viene ora usato nel titolo HTML e nei titoli Open Graph/Twitter;
- il `launch_mode: true` è rimasto attivo fino alla revisione finale.

Non è stata eseguita una compilazione Jekyll perché lo strumento non risulta disponibile nell'ambiente. Eseguire `bundle exec jekyll build` dopo aver reintegrato i file nel repository e verificare la home pubblicata.
