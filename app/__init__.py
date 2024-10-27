from flask import Flask
from app.users.routes import blueprint as user_blueprint
from app.posts.routes import blueprint as post_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)
