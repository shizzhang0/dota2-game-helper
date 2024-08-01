import logging
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
import gsi.handler as handler

log = logging.getLogger(__name__)


class GSIServer(ThreadingHTTPServer):
    def __init__(self, server_address, request_handler):
        super().__init__(server_address, request_handler)


class GSIRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            json_data = json.loads(post_data)
            handler.handle_game_state(json_data)
        except json.JSONDecodeError:
            log.error("invalid json received. raw data: %s", post_data.decode())

    def log_message(self, format, *args):
        """ don't use sys.stderr in pyinstaller with --noconsole"""
        return


class ServerManager:

    def __init__(self, ip='localhost', port=3000):
        self.ip = ip
        self.port = port
        self.thread = None
        self.server = GSIServer((ip, port), GSIRequestHandler)

    def run(self):
        log.info(f"dota2 gsi server listening on {self.ip}:{self.port}")
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        log.info("dota2 gsi server shutdown")
