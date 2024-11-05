from flask_migrate import Migrate
from kavenegar import KavenegarAPI
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

api_key = '6F31465A66545465455074695852747953343779454D786E7870726F6666592B686F4142744250584C67513D'
sms_api = KavenegarAPI(api_key)
migrate = Migrate(render_as_batch=True)