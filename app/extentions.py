from flask_migrate import Migrate
from kavenegar import KavenegarAPI
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

api_key = 'enter your own api key'
sms_api = KavenegarAPI(api_key)
migrate = Migrate(render_as_batch=True)
login_manager = LoginManager()