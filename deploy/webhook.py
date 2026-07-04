#!/usr/bin/env python3
"""OIR GitHub Webhook Handler.

Listens for push events from GitHub and triggers a site rebuild.
Runs as a systemd service behind nginx reverse proxy.

Security:
- Validates GitHub webhook signature (HMAC-SHA256)
- Only processes push events to the main branch
- Runs deploy.sh as a subprocess
"""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

OIR_ROOT = Path("/opt/oir")
REPO_DIR = OIR_ROOT / "repo"
DEPLOY_SCRIPT = REPO_DIR / "deploy" / "deploy.sh"
SECRET_FILE = OIR_ROOT / ".webhook-secret"
LOG_FILE = OIR_ROOT / "webhook.log"
# Default 127.0.0.1; production nginx-in-Docker needs 0.0.0.0 (see oir-webhook.service).
HOST = os.environ.get("WEBHOOK_HOST", "127.0.0.1")
PORT = int(os.environ.get("WEBHOOK_PORT", "9000"))

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("oir-webhook")


def load_secret() -> bytes:
    """Load the webhook secret from file."""
    if not SECRET_FILE.exists():
        logger.error(f"Webhook secret not found: {SECRET_FILE}")
        sys.exit(1)
    return SECRET_FILE.read_text().strip().encode()


def verify_signature(payload: bytes, signature: str, secret: bytes) -> bool:
    """Verify GitHub webhook HMAC-SHA256 signature."""
    if not signature.startswith("sha256="):
        return False
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)


class WebhookHandler(BaseHTTPRequestHandler):
    secret = load_secret()

    def do_POST(self):
        if self.path != "/webhook/deploy":
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers.get("Content-Length", 0))
        payload = self.rfile.read(content_length)

        # Verify signature
        signature = self.headers.get("X-Hub-Signature-256", "")
        if not verify_signature(payload, signature, self.secret):
            logger.warning("Invalid webhook signature — rejected")
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Invalid signature")
            return

        # Parse event
        event = self.headers.get("X-GitHub-Event", "")
        if event != "push":
            logger.info(f"Ignoring non-push event: {event}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Ignored")
            return

        # Check if push is to main branch
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            return

        ref = data.get("ref", "")
        if ref != "refs/heads/main":
            logger.info(f"Ignoring push to non-main branch: {ref}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Ignored (not main)")
            return

        # Trigger deploy
        logger.info(f"Push to main detected — triggering deploy...")
        try:
            result = subprocess.run(
                [str(DEPLOY_SCRIPT)],
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
            )
            if result.returncode == 0:
                logger.info("Deploy completed successfully")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Deploy successful")
            else:
                logger.error(f"Deploy failed: {result.stderr}")
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Deploy failed")
        except subprocess.TimeoutExpired:
            logger.error("Deploy timed out after 300s")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Deploy timed out")
        except Exception as e:
            logger.error(f"Deploy error: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Deploy error")

    def do_GET(self):
        """Health check endpoint."""
        if self.path == "/webhook/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        """Suppress default request logging (we use our own logger)."""
        logger.debug(f"{self.address_string()} - {format % args}")


def main():
    logger.info(f"OIR Webhook handler starting on {HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), WebhookHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Webhook handler shutting down")
        server.shutdown()


if __name__ == "__main__":
    main()
