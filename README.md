# RPI IEEE Student Branch — Website

A minimal starting point for the IEEE Student Branch website at Rensselaer Polytechnic Institute. Plain HTML/CSS/JS — no build step, no dependencies, deploys straight to GitHub Pages.

## Current state

This is intentionally stripped down: just the site's nav, page shells, and basic styling — no real content yet. Each page (`officers.html`, `calendar.html`, `nexus.html`, `join.html`, `contact.html`) has a heading and nothing else. Fill them in with real content when it's ready.

## Structure

```
index.html        Home
officers.html      Officer roster (empty)
calendar.html      Calendar (empty)
nexus.html         Articles / announcements (empty)
join.html          How to join (empty)
contact.html        Contact info (empty)
css/style.css      All styling (one file, uses CSS variables for theming)
js/main.js         Mobile nav toggle, active-link highlight, footer year
assets/            Favicon (SVG)
build.py           Script that generates the HTML pages
```

## Editing content

There's no templating system in the shipped HTML — each page repeats the header/footer directly, so nav/footer edits need to be made on all six pages (or edit the `HEADER`/`FOOTER` templates in `build.py` and rerun `python3 build.py` to regenerate everything at once).

To add content to a page, edit the `<main><div class="container"> ... </div></main>` block in that page's HTML.

## Styling

Everything is driven by CSS custom properties at the top of `css/style.css` (`:root { ... }`) — change `--color-primary`, `--color-bg`, etc. to retheme the whole site.

## Running locally

No build step needed. Either open `index.html` directly in a browser, or serve it so relative paths behave exactly like production:

```
python3 -m http.server 8000
```

## Deploying (GitHub Pages)

1. Push to GitHub.
2. In the repo, go to **Settings → Pages**.
3. Under "Build and deployment," set **Source** to "Deploy from a branch," branch **main**, folder **/(root)**.
4. Save. The site will be live at `https://<username>.github.io/<repo-name>/` within a minute or two.

No GitHub Actions workflow is required for this plain HTML/CSS/JS setup.
