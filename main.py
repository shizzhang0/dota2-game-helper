import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

from application import App
from gsi import gsi_server

def setup_logging():
    root_log = logging.getLogger()
    root_log.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(filename='app.log', when="D", interval=1, backupCount=3)
    # handler = RotatingFileHandler(filename='app.log', maxBytes=10 * 1024 * 1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root_log.addHandler(handler)

if __name__ == '__main__':
    setup_logging()
    gsi_server.run()
    app = App()
    app.mainloop()