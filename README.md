# Feuersetzen – Feuersetzparagenese Badenweiler

Statische Website zur Dokumentation der historischen Bergbautechnik des **Feuersetzens** und der daraus entstandenen **Feuersetzparagenese** am Beispiel von **Badenweiler** im südlichen Schwarzwald.

## Inhalt

- **Geschichte des Feuersetzens** – Von der Bronzezeit bis Agricola
- **Badenweiler – Geologie & Bergbau** – Das Quarzriff, Erzgänge, feuergesetzte Abbaue
- **Feuersetzparagenese** – Elyit (Leitmineral), Chenit, Caledonit, Lanarkit, Shannonit und weitere
- **Begleitende Mineralien** – Quarz, Baryt, Fluorit, Silber, Pyromorphit, Wulfenit und mehr
- **Museum & Wanderweg** – Der geologisch-montanhistorische Wanderweg und das Kurparkmuseum

## Tech-Stack

- [Astro](https://astro.build/) 5.x – Statische Site-Generierung
- Vanilla CSS – Dark Theme optimiert für Mineralfotografie
- Sharp – Bildoptimierung (WebP)
- GitHub Pages – Hosting

## Deployment (GitHub Pages)

- Im Repo: **Settings → Pages → Source** auf **GitHub Actions** stellen (nicht „Deploy from a branch“).
- Nach Push auf `main` baut der Workflow automatisch; die Seite ist dann unter:
  **https://astrogolem224.github.io/feuersetzen/**

## Entwicklung

```bash
npm install
npm run dev       # Dev-Server auf localhost:4321
npm run build     # Produktionsbuild nach dist/
npm run preview   # Vorschau des Builds
```

## Datenquelle

Die Inhalte basieren auf einer PowerPoint-Präsentation von Mineraliensammlern aus Badenweiler. Das Python-Script `build_content.py` extrahiert die Texte, Notizen und Bilder aus der PPTX-Datei und erzeugt die strukturierten Content-Dateien für Astro.

## Ergänzende Quellen

Recherchierte Zusatzinformationen stammen aus:

- [Wikipedia – Feuersetzen](https://de.wikipedia.org/wiki/Feuersetzen)
- [LGRB Baden-Württemberg](https://lgrbwissen.lgrb-bw.de/historische-bergbau-mineralien-badenweiler-im-schwarzwald)
- [Schwarzwald-Mineralien.de](http://www.schwarzwald-mineralien.de/Badenweiler_Galerie.html)
- [Clara-Mineralien.de](http://www.clara-mineralien.de/blackforest/blackforestsouth/bergbau-in-badenweiler.html)
- [Mindat.org](https://www.mindat.org/)

Ergänzende Inhalte sind auf der Website als solche markiert und mit Quellenangaben versehen.

## Lizenz

Inhalte und Bilder: Eigentum der jeweiligen Autoren/Fotografen.
Code: ISC License.
