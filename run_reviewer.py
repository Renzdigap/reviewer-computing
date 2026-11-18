#!/usr/bin/env python3
"""
Master Launcher for Huawei ICT Competition National Stage Study Reviewer
Run with: py run_reviewer.py
"""
import functools
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))

PILLARS = [
    ("01-HCIA-Computing-V3.0", "Pillar 1: HCIA-Computing V3.0 (Kunpeng & Server Ecosystem)"),
    ("02-HCIA-openEuler-V2.0", "Pillar 2: HCIA-openEuler V2.0 (openEuler OS, Shell & iSula)"),
    ("03-HCIA-openGauss-V2.0", "Pillar 3: HCIA-openGauss V2.0 (openGauss Database, SQL & GaussDB)")
]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_local_server():
    handler = functools.partial(QuietHandler, directory=ROOT)
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    url = f"http://127.0.0.1:{port}/index.html"
    print(f"\n🌐 Serving Reviewer at {url} (Press Ctrl+C or quit to stop)")
    webbrowser.open(url)
    return httpd


def main():
    httpd = None
    try:
        while True:
            print("\n" + "=" * 78)
            print("  HUAWEI ICT COMPETITION (COMPUTING TRACK) — NATIONAL STAGE STUDY REVIEWER")
            print("=" * 78)
            print("  [0] 🌐 Launch Local Web Server + Open Master Hub (Recommended for progress sync)")
            print("  [f] 📂 Open index.html directly via file://")
            for idx, (folder, label) in enumerate(PILLARS, 1):
                print(f"  [{idx}] 📚 Launch {label} (Terminal CLI Mode)")
            print("  [q] Quit")
            c = input("\nSelect an option: ").strip().lower()
            if c == "q":
                break
            elif c == "0":
                if httpd is None:
                    httpd = start_local_server()
                else:
                    port = httpd.server_address[1]
                    webbrowser.open(f"http://127.0.0.1:{port}/index.html")
            elif c == "f":
                webbrowser.open(os.path.join(ROOT, "index.html"))
            elif c in ("1", "2", "3"):
                folder = PILLARS[int(c) - 1][0]
                cli_path = os.path.join(ROOT, folder, "practice_cli.py")
                subprocess.run([sys.executable, cli_path])
    finally:
        if httpd is not None:
            httpd.shutdown()


if __name__ == "__main__":
    main()
