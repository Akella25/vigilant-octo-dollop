import os
from flask import Flask


def create_app():
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)

    from . import task
    app.register_blueprint(task.bp)

    return app