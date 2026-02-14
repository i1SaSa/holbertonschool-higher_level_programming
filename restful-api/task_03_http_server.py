import http.server
import socketserver
import json

PORT = 8000


class MySimpleAPI(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_response = json.dumps(data).encode('utf-8')
            self.wfile.write(json_response)

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))


with socketserver.TCPServer(("", PORT), MySimpleAPI) as httpd:
    print(f"Serving at port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
