from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.users.routes import blueprint as user_blueprint
from app.posts.routes import blueprint as post_blueprint
import app.exceptions as error_handler


def register_blueprint(app):
    app.register_blueprint(user_blueprint)
    app.register_blueprint(post_blueprint)


def register_error_handlers(app):
    app.register_error_handler(404, error_handler.page_not_found)
    app.register_error_handler(500, error_handler.server_error)


app = Flask(__name__)
register_blueprint(app)
register_error_handlers(app)
app.config.from_object('config.DevConfig')

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
