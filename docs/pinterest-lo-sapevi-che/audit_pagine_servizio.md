# Audit pagine di servizio — FluenteMente

Data revisione: 21 ottobre 2026.

## Pagine generate

| File | URL previsto | Stato contenuto |
|---|---|---|
| `pages/servizi/chi-siamo.md` | `/chi-siamo/` | Bozza editoriale completa; nome del responsabile e email da inserire. |
| `pages/servizi/privacy.md` | `/privacy/` | Informativa orientativa basata sul repository e sulla documentazione pubblica dell'hosting; titolare, recapiti, tempi di conservazione e trasferimenti da verificare. |
| `pages/servizi/cookie.md` | `/cookie/` | Bozza basata su ispezione statica; l'inventario reale va ottenuto testando il sito online. |
| `pages/servizi/disclaimer.md` | `/disclaimer/` | Pagina Affiliazioni collegata al footer e all'include; aggiornata per dichiarare il link Awin verso Babbel, da verificare prima della pubblicazione live. |

## Risultati dal repository statico

- La configurazione esaminata nella revisione del 21 ottobre 2026 indicava GitHub Pages/Jekyll e `launch_mode: true`; il valore è stato aggiornato successivamente, come riportato nella nota di stato in fondo a questo file.
- Non sono stati trovati nel codice esaminato script espliciti per analytics, retargeting o pixel pubblicitari, né form di contatto/newsletter o contenuti social incorporati.
- Il footer contiene già i collegamenti a `/chi-siamo/`, `/privacy/`, `/cookie/` e `/disclaimer/`.
- Il componente di disclosure viene ora mostrato solo se richiesto tramite `show_affiliate_disclosure: true`, invece di apparire indiscriminatamente sulle pagine ordinarie.
- Il link del layout legacy `_layouts/curiosita.html` è stato indirizzato all’articolo esistente `/come-studiare-inglese-ogni-giorno/`, evitando una destinazione senza pagina nel pacchetto.
- È configurato un URL affiliato Awin verso Babbel nell'articolo dedicato; prima della pubblicazione live vanno testati redirect e tracciamento.

## Limitazioni

Non sono stati verificati cookie sulla versione live, non sono stati testati i servizi esterni mediante browser e non è stato eseguito un build Jekyll. La sola ispezione dei file non conferma l'effettivo comportamento del dominio pubblicato. I campi evidenziati devono essere completati prima della messa online.


## Aggiornamento stato indicizzazione — 25 ottobre 2026

La nota relativa a `launch_mode: true` descrive lo stato rilevato nell'audit originale. La configurazione corrente è stata successivamente aggiornata a `launch_mode: false`: i contenuti editoriali possono essere indicizzati. Le pagine Privacy, Cookie, Chi siamo e Affiliazioni rimangono temporaneamente `noindex, follow` ed escluse dalla sitemap finché i campi e i controlli non sono completati. La build e la verifica live devono ancora essere eseguite dopo il deploy.
