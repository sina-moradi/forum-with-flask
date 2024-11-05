from app.databases import BaseModel
from app.extentions import db


class User(BaseModel):
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=True)
    phone = db.Column(db.String(11), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.id} {self.username})'


class SmsCode(BaseModel):
    number = db.Column(db.Integer)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    expire_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.id} {self.number})'
    