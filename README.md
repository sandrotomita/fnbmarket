# fnbmarket

**Food Ingredients 2036**: a market vision for the food and beverage ingredients industry, by Sandro Sato Tomita.

Static website: plain HTML and CSS, no framework. The deployable site is in `public/`.

## Edit the content

| What | Where |
|---|---|
| Vision, findings, scenarios, impact, strategy, consumer page, sources | `content.py` |
| Bio / About me page | `content/bio.html` |
| Design (colours, fonts, layout) | `public/assets/styles.css` |
| Images | `public/assets/` |

After editing, rebuild the pages (requires Python 3):

```sh
python3 build_pages.py
```

Then commit and push. Commit the regenerated `public/` folder too.

## Preview locally

```sh
python3 -m http.server -d public 8000
# open http://localhost:8000
```

## Deploy (Cloudflare Workers, static assets)

`wrangler.jsonc` points Cloudflare at `public/`.

1. Cloudflare dashboard → **Workers & Pages → Create → Import a repository** → select `sandrotomita/fnbmarket`.
2. Build command: leave empty. Deploy command: `npx wrangler deploy`.
3. Add a custom domain under the Worker's **Settings → Domains & Routes**.

Every push to `main` redeploys the site.

## Note

All 2036 statements are scenarios, not predictions. Sources are listed on `sources.html`.
