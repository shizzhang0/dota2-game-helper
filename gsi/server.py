import logging
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from gsi.handler import game_state_handler

log = logging.getLogger(__name__)


class GSIServer(HTTPServer):
    def __init__(self, server_address, request_handler):
        super().__init__(server_address, request_handler)


class GSIRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            json_data = json.loads(post_data)
            # TODO: test
            json_data = json.loads(json_data)
            game_state_handler.handle(json_data)
        except json.JSONDecodeError:
            log.error(f"fail to load json : {post_data.decode()}")

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


gsi_server = ServerManager()
