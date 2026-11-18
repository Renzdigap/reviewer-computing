#!/usr/bin/env python3
"""
Master Launcher & Local Server for Huawei ICT Competition National Stage Study Reviewer
Features:
- Fixed-port HTTP server (defaults to 8080) for stable browser origin
- /api/progress endpoint: persists progress strictly to local progress.json on this PC
- Keeps your study progress completely private/local so teammates can use the repo independently
Run with: py run_reviewer.py
"""
import functools
import http.server
import json
import os
import socketserver
import subprocess
import sys
import threading
import webbrowser

import progress_manager

ROOT = os.path.dirname(os.path.abspath(__file__))

PILLARS = [
    ("01-HCIA-Computing-V3.0", "Pillar 1: HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)"),
    ("02-HCIA-openEuler-V2.0", "Pillar 2: HCIA-openEuler V2.0 (openEuler OS, Shell & iSula)"),
    ("03-HCIA-openGauss-V2.0", "Pillar 3: HCIA-openGauss V2.0 (openGauss Database, SQL & GaussDB)")
]

DEFAULT_PORT = 8080


class LocalReviewerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def log_message(self, format, *args):
        # Keep terminal clean; suppress standard GET/POST file logs
        pass

    def send_json(self, status_code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/api/progress":
            data = progress_manager.get_progress()
            self.send_json(200, data)
        elif path == "/api/status":
            self.send_json(200, {"status": "running", "root": ROOT})
        else:
            super().do_GET()

    def do_POST(self):
        path = self.path.split("?")[0]
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len) if content_len > 0 else b"{}"

        if path == "/api/progress":
            try:
                payload = json.loads(body.decode("utf-8"))
                incoming = payload.get("progress", payload)
                saved = progress_manager.merge_and_save(incoming)
                self.send_json(200, {"status": "ok", "last_synced": saved.get("last_synced")})
            except Exception as e:
                self.send_json(400, {"status": "error", "message": str(e)})
        else:
            self.send_json(404, {"status": "not_found"})


def start_local_server():
    port = DEFAULT_PORT
    httpd = None
    # Attempt binding starting from DEFAULT_PORT
    for try_port in range(DEFAULT_PORT, DEFAULT_PORT + 20):
        try:
            httpd = socketserver.TCPServer(("127.0.0.1", try_port), LocalReviewerHandler)
            port = try_port
            break
        except OSError:
            continue

    if httpd is None:
        # Fallback to ephemeral port if range 8080-8100 is completely blocked
        httpd = socketserver.TCPServer(("127.0.0.1", 0), LocalReviewerHandler)
        port = httpd.server_address[1]

    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    url = f"http://127.0.0.1:{port}/index.html"
    print(f"\n🌐 Serving Reviewer at: {url}")
    print(f"💾 Local PC Storage: {progress_manager.PROGRESS_FILE}")
    print("🔒 Private: Progress stays strictly on this machine (ignored by Git)")
    webbrowser.open(url)
    return httpd, port


def main():
    httpd = None
    server_port = None
    try:
        while True:
            curr_prog = progress_manager.get_progress().get("progress", {})
            total_saved = len(curr_prog)
            print("\n" + "=" * 78)
            print("  HUAWEI ICT COMPETITION (COMPUTING TRACK) — STUDY REVIEWER")
            print("=" * 78)
            server_status = f"Running on http://127.0.0.1:{server_port}" if httpd else "Not running"
            print(f"  Status: Web Server [{server_status}] | Local Progress Units Saved: [{total_saved}]")
            print("  Storage: Strictly Local PC (progress.json is gitignored for teammate privacy)")
            print("-" * 78)
            print("  [0] 🌐 Launch / Open Web Platform in Browser (Saves locally to progress.json)")
            print("  [f] 📂 Open index.html directly via file://")
            for idx, (folder, label) in enumerate(PILLARS, 1):
                print(f"  [{idx}] 📚 Launch {label} (Terminal CLI Mode)")
            print("  [r] 🗑️  Reset Local Progress (Clear study history on this PC)")
            print("  [q] Quit")
            c = input("\nSelect an option: ").strip().lower()
            if c == "q":
                break
            elif c == "0":
                if httpd is None:
                    httpd, server_port = start_local_server()
                else:
                    url = f"http://127.0.0.1:{server_port}/index.html"
                    print(f"\nRe-opening browser at {url}...")
                    webbrowser.open(url)
            elif c == "f":
                p = os.path.join(ROOT, "index.html")
                webbrowser.open(p)
                print(f"\nOpened {p}")
            elif c == "r":
                confirm = input("Are you sure you want to reset all your local progress? (y/N): ").strip().lower()
                if confirm == "y":
                    progress_manager.reset_local_progress()
                    print("✅ Local progress has been reset to zero.")
            elif c in ["1", "2", "3"]:
                folder = PILLARS[int(c) - 1][0]
                script = os.path.join(ROOT, folder, "practice_cli.py")
                subprocess.run([sys.executable, script])
            else:
                print("Invalid selection.")
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        if httpd:
            httpd.shutdown()


if __name__ == "__main__":
    main()
