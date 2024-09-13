from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class HTTPRequestHandler(BaseHTTPRequestHandler):
    # GET method
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello, RAJVEER "
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

# Server settings
server_address = ('127.0.0.1', 8080)
httpd = HTTPServer(server_address, HTTPRequestHandler)

# Start the HTTP server
print('Starting server...')
httpd.serve_forever()

#http://127.0.0.1:8080/ port