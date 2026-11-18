#!/usr/bin/env python3
"""
Master Launcher & Sync Server for Huawei ICT Competition National Stage Study Reviewer
Features:
- Fixed-port HTTP server with auto-discovery (defaults to 8080)
- /api/progress endpoint: persists progress to progress.json on disk
- /api/git-sync endpoint: automatically stages, commits, and pushes progress to GitHub
- Terminal CLI practice mode with direct progress.json synchronization
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


class SyncReviewerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def log_message(self, format, *args):
        # Keep console clean; log only API calls if needed
        if args and any(api in str(args[0]) for api in ["/api/"]):
            sys.stdout.write(f"\r[Server API] {args[0]}\nSelect an option: ")
            sys.stdout.flush()

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

        elif path == "/api/git-sync":
            try:
                ok, msg = progress_manager.git_sync_progress()
                self.send_json(200 if ok else 500, {"status": "ok" if ok else "error", "message": msg})
            except Exception as e:
                self.send_json(500, {"status": "error", "message": str(e)})
        else:
            self.send_json(404, {"status": "not_found"})


def start_local_server():
    port = DEFAULT_PORT
    httpd = None
    # Attempt binding starting from DEFAULT_PORT
    for try_port in range(DEFAULT_PORT, DEFAULT_PORT + 20):
        try:
            httpd = socketserver.TCPServer(("127.0.0.1", try_port), SyncReviewerHandler)
            port = try_port
            break
        except OSError:
            continue

    if httpd is None:
        # Fallback to ephemeral port if range 8080-8100 is completely blocked
        httpd = socketserver.TCPServer(("127.0.0.1", 0), SyncReviewerHandler)
        port = httpd.server_address[1]

    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    url = f"http://127.0.0.1:{port}/index.html"
    print(f"\n🌐 Serving Reviewer at: {url}")
    print(f"💾 Persistent Progress Store: {progress_manager.PROGRESS_FILE}")
    print(f"🔄 Real-Time Disk Sync & API Active on port {port}")
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
            print("  HUAWEI ICT COMPETITION (COMPUTING TRACK) — STUDY REVIEWER & SYNC HUB")
            print("=" * 78)
            server_status = f"Running on http://127.0.0.1:{server_port}" if httpd else "Not running"
            print(f"  Status: Web Server [{server_status}] | Progress Entries Saved: [{total_saved}]")
            print("-" * 78)
            print("  [0] 🌐 Launch / Open Web Platform in Browser (Persistent Sync to progress.json)")
            print("  [s] 🔄 Git Sync Now (Commit & Push progress.json to GitHub)")
            print("  [f] 📂 Open index.html directly via file://")
            for idx, (folder, label) in enumerate(PILLARS, 1):
                print(f"  [{idx}] 📚 Launch {label} (Terminal CLI Mode)")
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
            elif c == "s":
                print("\nInitiating automatic Git Commit & Push for progress.json...")
                ok, msg = progress_manager.git_sync_progress()
                print(("✅ " if ok else "⚠️ ") + msg)
            elif c == "f":
                p = os.path.join(ROOT, "index.html")
                webbrowser.open(p)
                print(f"\nOpened {p}")
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
