from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), MyHandler)
    print(f"Server running at http://{host}:{port}/")
    server.serve_forever()