# FluenteMente — configurazione di indicizzazione

Data: 25 ottobre 2026

## Modifiche applicate

- In `_config.yml`, `launch_mode: false` abilita il meta robots `index, follow` per gli articoli e le pagine editoriali pubbliche.
- La sitemap viene generata dal plugin Jekyll `jekyll-sitemap` configurato nel repository. Non è stato aggiunto un `robots.txt` nella sottocartella del progetto: per Google quel file deve stare alla radice dell’host e una copia sotto `/FluenteMente/` non controllerebbe il crawling del dominio.
- `_includes/head.html` rispetta il valore `page.robots` e non emette il canonical quando `page.no_canonical` è attivo.
- La pagina `/404.html` resta `noindex, follow`, senza canonical e senza inclusione in sitemap.
- `pages/servizi/privacy.md`, `pages/servizi/cookie.md`, `pages/servizi/chi-siamo.md` e `pages/servizi/disclaimer.md` restano temporaneamente `noindex, follow` ed escluse dalla sitemap perché contengono campi non completati o verifiche tecniche da fare.

## Azioni ancora necessarie prima del deploy definitivo

1. Completare nome/denominazione e recapiti reali nelle pagine di servizio; non lasciare i campi tra parentesi quadre.
2. Verificare l'informativa cookie con un browser pulito e confermare quali strumenti e richieste di rete siano effettivamente attivi.
3. Eseguire la build GitHub Actions e verificare la versione generata di `sitemap.xml`, canonical e meta robots. Se si desidera un `robots.txt` per l’intero host `nausica-c.github.io`, va gestito alla radice dell’host e non dentro questa repository di progetto.
4. Dopo la revisione delle pagine di servizio, rimuovere `robots: "noindex, follow"` e `sitemap: false` da ciascuna pagina completata, in modo da includerla nella sitemap.
5. Dopo il deploy, aprire `https://nausica-c.github.io/FluenteMente/sitemap.xml`, inviarla in Google Search Console se la proprietà è verificata e controllare eventuali errori di scansione e indicizzazione.

## Limiti

Queste modifiche rendono il repository predisposto all'indicizzazione, ma non inviano automaticamente un nuovo deploy a GitHub né chiedono a Google di indicizzare subito gli URL. La build completa non è stata eseguita nell'ambiente corrente.
