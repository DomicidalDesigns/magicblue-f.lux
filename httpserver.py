import http.server
import socketserver

PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    import sys
    buffer = 1
    sys.stderr = open('flux.txt', 'w', buffer)
    httpd.serve_forever()
