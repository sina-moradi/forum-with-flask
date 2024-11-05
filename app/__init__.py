from flask import Flask

from app.users.routes import blueprint as user_blueprint
from app.posts.routes import blueprint as post_blueprint
import app.exceptions as error_handler
from app.extentions import migrate, db


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

db.init_app(app)
from app.users.models import User  # is here due to circular_imports for db.create_all() use
migrate.init_app(app, db)
