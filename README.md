# HobbyMall

A multi-category hobby marketplace for India — diecast, model kits, DIY
craft, and more, built as a top-down learning project: domain → hosting →
DevOps → microservices → MCP → agentic chatbot.

## What's here right now

This is the **walking skeleton** — the thinnest possible service, deployed
through the entire pipeline, before anything real gets built:

- `app.py` — one Flask route, `/health`, returns `{"status": "ok"}`
- `Dockerfile` — packages it into a container
- `docker-compose.yml` — how it'll run on the VPS
- `.github/workflows/ci.yml` — builds the image and publishes it to GitHub
  Container Registry on every push to `main`

The point isn't the app — it's proving that a push to `main` reliably turns
into a running container. Everything after this (Catalog, Orders, Auth,
MCP server, the chatbot) gets built the same way, once this one is proven.

## Running it locally

```bash
docker compose up --build
curl http://localhost:8000/health
```

## Deploying (dev phase: your laptop stands in for the VPS)

Provisioning a real VPS costs money you don't need to spend yet to prove
the pipeline. Instead, `.github/workflows/ci.yml` has a `deploy` job that
runs on a **self-hosted GitHub Actions runner** — your laptop — so
`git push` still triggers a real build-and-deploy, it just deploys to
`localhost:8000` on your machine instead of a cloud box.

That needs two things running persistently on your laptop, outside of
this repo:
1. A **self-hosted Actions runner**, registered to this repo, so GitHub
   can hand it the `deploy` job
2. A **Cloudflare quick tunnel** (`cloudflared tunnel --url
   http://localhost:8000`), so the container is reachable at a public
   HTTPS URL instead of only `localhost`

Neither of those lives in this repo — they're processes on your machine,
not files to commit.

## Moving to a real VPS later

Nothing here changes structurally — swap the self-hosted runner (or the
`deploy` job's `docker run` step, via SSH) to point at the VPS instead of
your laptop, and the exact same pipeline ships there instead.

## What's not here yet

- A VPS (Phase 1) — deliberately deferred, see above
- Everything past the walking skeleton — Catalog/Orders services, Postgres,
  object storage, Redis, the MCP server, the chatbot
