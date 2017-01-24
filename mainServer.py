import config
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class mySafeHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # No built in logs.
        return

    def do_GET(self):
        # Handler for the GET requests
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World ! your path: " + self.path)
        return


try:
    server = HTTPServer(("", config.SERVER_PORT), mySafeHandler)
    print 'Started httpserver on port ', config.SERVER_PORT

    # Start server
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
