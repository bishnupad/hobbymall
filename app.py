"""HobbyMall walking-skeleton service.

This is deliberately the thinnest possible Flask app — one route, no
database, no business logic. Its only job is to prove the full pipeline
works end to end: domain -> server -> container -> CI/CD -> live URL.
Real services (Catalog, Orders, ...) get built the same way once this
one is proven live.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok", service="hobbymall-skeleton")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
