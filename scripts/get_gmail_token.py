#!/usr/bin/env python3
"""One-time helper: mint a Gmail refresh token for the morning digest.

Run this once on your own machine (not in CI). It opens a browser, asks you
to grant access to your own Gmail, and prints the refresh token to paste into
GitHub repo secrets.

    pip install requests
    python scripts/get_gmail_token.py

You need an OAuth client id and secret first — see scripts/README.md.
"""

from __future__ import annotations

import http.server
import secrets
import socketserver
import sys
import urllib.parse
import webbrowser

import requests

AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
PORT = 8765
REDIRECT_URI = f"http://localhost:{PORT}"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

received: dict[str, str] = {}


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        received.update({k: v[0] for k, v in params.items()})

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        ok = "code" in received
        self.wfile.write(
            (
                "<h2>Done — you can close this tab.</h2>"
                if ok
                else "<h2>Something went wrong. Check the terminal.</h2>"
            ).encode()
        )

    def log_message(self, *args):  # silence the default request logging
        pass


def main() -> None:
    client_id = input("OAuth client id: ").strip()
    client_secret = input("OAuth client secret: ").strip()
    if not client_id or not client_secret:
        sys.exit("Both the client id and secret are required.")

    state = secrets.token_urlsafe(16)
    params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        # Both are needed or Google withholds the refresh token on re-consent.
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
    }
    url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    print(f"\nOpening your browser. If it does not open, visit:\n{url}\n")
    webbrowser.open(url)

    with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
        httpd.handle_request()

    if received.get("state") != state:
        sys.exit("State mismatch — start over.")
    if "code" not in received:
        sys.exit(f"No authorization code returned: {received}")

    resp = requests.post(
        TOKEN_URL,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": received["code"],
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
        },
        timeout=45,
    )
    if resp.status_code != 200:
        sys.exit(f"Token exchange failed ({resp.status_code}): {resp.text[:400]}")

    refresh_token = resp.json().get("refresh_token")
    if not refresh_token:
        sys.exit(
            "Google returned no refresh token. This happens when the app was "
            "already authorized — revoke it at "
            "https://myaccount.google.com/permissions and run this again."
        )

    print("\n" + "=" * 62)
    print("Add these three as GitHub repo secrets:\n")
    print(f"GMAIL_CLIENT_ID      {client_id}")
    print(f"GMAIL_CLIENT_SECRET  {client_secret}")
    print(f"GMAIL_REFRESH_TOKEN  {refresh_token}")
    print("=" * 62)
    print("\nTreat the refresh token like a password. It grants read and send")
    print("access to your mailbox until you revoke it.")


if __name__ == "__main__":
    main()
