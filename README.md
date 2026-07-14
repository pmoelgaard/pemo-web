# pemo-web

Professional profile page for **Peter A. Moelgaard**, served at
[www.pemo.me](https://www.pemo.me) (and the apex `pemo.me`).

## Stack

- Static pages — no build step, no dependencies.
  - `public/index.html` — landing page: masonry gallery of projects, fed by
    `public/assets/projects.json` (placeholder data for now; regenerate with
    `python3 scripts/generate_projects.py`).
  - `public/contact/index.html` — contact module, served at `/contact`
    (redirects to `/contact/` via the Worker's `auto-trailing-slash` handling).
- Hosted as the Cloudflare Worker **pemo-www** (static assets), with
  `pemo.me` and `www.pemo.me` attached as custom domains. Cloudflare issues
  and auto-renews the TLS certificate.
- Contact links and QR codes point at the existing `go.pemo.me/*` short links.

## Deploy

Pushes to `main` deploy automatically via GitHub Actions
(`.github/workflows/deploy.yml`), using the `CLOUDFLARE_API_TOKEN` repository
secret (a Cloudflare API token with *Edit Cloudflare Workers* permissions).

Manual deploy:

```sh
npx wrangler deploy
```

## Local preview

```sh
npx wrangler dev --port 8642
# open http://localhost:8642
```

Runs the real Workers assets pipeline locally (trailing-slash handling, SPA
fallback), so routes behave exactly as in production. Also wired up as the
`pemo-www` launch configuration in `.claude/launch.json`.

## History

Migrated on 2026-07-13 from a Gamma-hosted site (`sites.gamma.app`) after its
TLS certificate expired and broke the domain.
