# Seteo de la aplicación
from flask import Flask
from views import set_views


def create_app():
    """ Inicializa la aplicación web, configura las rutas """
    app = Flask(__name__, static_folder="static")
    set_views(app)
    # acá va cualquier otro set que necesite

    return app


app = create_app()
