# pemo-web

Professional profile page for **Peter A. Moelgaard**, served at
[www.pemo.me](https://www.pemo.me) (and the apex `pemo.me`).

## Stack

- Single static page (`public/index.html`) — no build step, no dependencies.
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
python3 -m http.server 8000 --directory public
# open http://localhost:8000
```

## History

Migrated on 2026-07-13 from a Gamma-hosted site (`sites.gamma.app`) after its
TLS certificate expired and broke the domain.
