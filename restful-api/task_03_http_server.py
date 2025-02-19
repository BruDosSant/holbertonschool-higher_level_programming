#!/usr/bin/python3
import http.server
import socketserver

class FrogHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")

host = "localhost"
PORT = 8000

with socketserver.TCPServer((host, PORT), FrogHandler) as httpd:
    print(f"Serving on {host}:{PORT}")
    httpd.serve_forever()
