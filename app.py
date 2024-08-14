import os
import threading
import time
import webbrowser

from flask import Flask

from database.db import create_database
from route import create_routes

app = Flask(__name__, template_folder='templates', static_folder='static')

create_routes(app)


def open_browser():
    time.sleep(5)
    webbrowser.open('http://127.0.0.1:5000')


if __name__ == '__main__':
    if not os.path.exists('contatos.db'):
        create_database()
    else:
        print("O banco de dados já existe.")
    threading.Thread(target=open_browser).start()
    app.run()
