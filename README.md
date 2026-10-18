# FluenteMente — repository integrato

Repository Jekyll per GitHub Pages che integra la base grafica pulita con i contenuti editoriali attuali e il funnel dei 30 Pin Pinterest “Lo sapevi che…?”.

## Stato attuale

- Brand: **FluenteMente**.
- URL GitHub Pages: `https://nausica-c.github.io/FluenteMente/`.
- Struttura editoriale della Fase 3 conservata, inclusi i permalink delle pagine e i dati dei 30 Pin.
- Base grafica (CSS, homepage, layout, 404) applicata; header e footer sono collegati agli hub reali e alle pagine legali presenti.
- Modalità `launch_mode: true`: la build genera `noindex, nofollow` finché non si decide di lanciare la nuova struttura.
- Analytics legacy non attivi nell'head; configurare consenso e informative prima di riattivarli.

## Prima del rilascio

1. Aprire `docs/editorial/struttura-repository-integrata.md`.
2. Controllare `docs/editorial/riconciliazione-primi-10-articoli.md` per evitare pagine duplicate.
3. Verificare tutti i link interni e i 30 percorsi in `docs/pinterest/30-pin-publishing.csv`.
4. Eseguire la build tramite GitHub Actions e controllare la versione su GitHub Pages.
5. Aggiornare Privacy/Cookie/Disclaimer in base agli strumenti effettivamente attivi.
6. Quando si è pronti all'indicizzazione, impostare `launch_mode: false`.

## Documenti editoriali

- `docs/editorial/brief-editoriali-30-pin-lo-sapevi-che.md`
- `docs/editorial/confronto-10-brief-vs-30-pin.md`
- `docs/editorial/mappa-destinazioni-30-pin.md`
- `docs/editorial/riconciliazione-primi-10-articoli.md`
- `docs/editorial/struttura-repository-integrata.md`
