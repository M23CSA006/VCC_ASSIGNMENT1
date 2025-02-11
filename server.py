from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "Hello from Microservice!", "status": "success"}
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if _name_ == "_main_":
    server_address = ("0.0.0.0", 5000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Microservice running on port 5000...")
    httpd.serve_forever()
