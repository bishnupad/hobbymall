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

## What's not here yet

- A VPS to actually deploy to (Phase 1) — once it exists, the CI workflow
  gets one more step: SSH in and `docker compose pull && docker compose up -d`
- Everything past the walking skeleton — Catalog/Orders services, Postgres,
  object storage, Redis, the MCP server, the chatbot
