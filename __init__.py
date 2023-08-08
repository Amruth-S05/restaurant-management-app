import os

from flask import Flask, redirect
from .config import Config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .blueprints import (
        home,
        menu,
        order,
    )
    app.register_blueprint(home.bp)
    app.register_blueprint(menu.bp)
    app.register_blueprint(order.bp)

    @app.route("/")
    def index():
        return redirect("/home", 302)

    return app
