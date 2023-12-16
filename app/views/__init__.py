# El manejo de rutas de la aplicación
from flask import render_template


def set_views(app) -> None:
    """ Configura las rutas de la aplicación """
    @app.route("/")
    def index():
        """ Ruta principal """
        return render_template("pages/index.html")
