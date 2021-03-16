from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request", self.request)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello World!</h1>")


if __name__ == "__main__":
    server = ThreadingHTTPServer(('localhost', 10_000), Handler)
    server.serve_forever()
