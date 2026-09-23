# RPI IEEE Student Branch — Website

A fresh, modern rebuild of the IEEE Student Branch website at Rensselaer Polytechnic Institute. Plain HTML/CSS/JS — no build step, no dependencies, deploys straight to GitHub Pages.

## Where the content came from

The branch no longer had admin access to its previous site (`sites.ecse.rpi.edu/ieee`), so this rebuild uses that old site's **public** content and page structure as a reference (mission statement, officer names/titles, contact emails, calendar embed, article topics) with an entirely new visual design.

**Before you launch this, an officer should double-check and update:**
- `officers.html` — the officer roster was pulled from the old site and may be out of date.
- `contact.html` — verify the listed emails (`ieee@rpi.edu`, `kingd7@rpi.edu`, `chene8@rpi.edu`) are still correct.
- `calendar.html` — confirm the embedded Google Calendar (`ieee.eps.rpi@gmail.com`) is still the branch's active calendar and is shared publicly (Google Calendar → Settings → that calendar → "Access permissions" → "Make available to public").
- `nexus.html` / the "Latest from Nexus" section on `index.html` — these are starter/placeholder article cards carried over from the old site's post titles. Replace them with real posts as you publish.

## Structure

```
index.html        Home
officers.html      Officer roster
calendar.html      Embedded Google Calendar
join.html          How to join (steps + IEEE membership link)
nexus.html         Articles / announcements
contact.html        Contact info + Discord/LinkedIn
css/style.css      All styling (one file, uses CSS variables for theming)
js/main.js         Mobile nav, fade-in animation, footer year, newsletter form stub
assets/            Favicon / logo mark (SVG)
```

There's no templating system — each page repeats the header/footer HTML directly, so edits to nav or footer content need to be made on all six pages. (`build.py` at the repo root is the script originally used to generate the pages; you can use it as a shortcut to regenerate all pages after editing the shared `HEADER`/`FOOTER` templates inside it, or just ignore/delete it and edit the HTML files directly.)

## Editing content

- **Officers**: edit the `branch_officers` / `eps_officers` lists in `build.py` (then rerun `python3 build.py`), or edit `officers.html` directly.
- **Colors/fonts/theme**: everything is driven by CSS custom properties at the top of `css/style.css` (`:root { ... }`) — change `--color-primary`, `--color-accent`, etc. to retheme the whole site at once.
- **New Nexus article**: duplicate one `.card.article-card` block in `nexus.html` (and optionally add it to the homepage preview section).

## Running locally

No build step needed. Either open `index.html` directly in a browser, or serve it so relative paths behave exactly like production:

```
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploying (GitHub Pages)

1. Push this repo to GitHub (already done if you're reading this from the repo).
2. In the repo, go to **Settings → Pages**.
3. Under "Build and deployment", set **Source** to "Deploy from a branch", branch **main**, folder **/(root)**.
4. Save. The site will be live at `https://<username>.github.io/<repo-name>/` within a minute or two.

No GitHub Actions workflow is required for this plain HTML/CSS/JS setup.

## Notes

- This is an unofficial, student-run site — not an official RPI or IEEE web property (see footer disclaimer).
- The newsletter signup in the footer is a visual stub (`js/main.js`) — wire it up to a real provider (Mailchimp, ConvertKit, Google Forms, etc.) before relying on it.
- Officer avatars are generated from initials — swap in real photos by replacing the `.avatar` div in `officers.html`/`build.py` with an `<img>`.
