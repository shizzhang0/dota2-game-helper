from application import App
from gsi import gsi_server

if __name__ == '__main__':
    gsi_server.run()
    app = App()
    app.mainloop()