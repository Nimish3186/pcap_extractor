from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"""
            <html>
            <body>
                <h2>Login Form</h2>
                <form method="POST">
                    Username: <input type="text" name="username"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit">
                </form>
            </body>
            </html>
        """)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Captured Data:", post_data.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Login received")

server = HTTPServer(('localhost', 8000), SimpleHandler)
print("Server running on http://localhost:8000")
server.serve_forever()