import os

from flask import Flask

from database.db import create_database

app = Flask(__name__)

if __name__ == '__main__':
    if not os.path.exists('contatos.db'):
        create_database()
    else:
        print("O banco de dados já existe.")
    app.run()
