import config
import json
import traceback
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class mySafeHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # No built in logs.
        return

    def do_GET(self):
        # Send help message for usage.

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(config.HELP_MESSAGE)
        return

    def jsonHeaders(self, statuscode):
        # General start for any response
        self.send_response(statuscode)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        try:
            bodyContent = self.rfile.read(int(self.headers['Content-Length']))
            jsonBody = json.loads(bodyContent)

            self.jsonHeaders(200)
        except Exception as ex:
            if (config.DETAILED_ERRORS):
                self.jsonHeaders(500)
                self.wfile.write(
                    json.dumps(
                        {"error": ex.message, "traceback": traceback.format_exc(config.STACK_TRACE_LIMIT)}
                    )
                )
            else:
                self.send_error(500, "Error handling POST in main module")
        return


try:
    server = HTTPServer(("", config.SERVER_PORT), mySafeHandler)
    print 'Started server on port ', config.SERVER_PORT

    # Start server
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
