from app import db


class BaseModel(db.Model):
    """ abstract class for all models """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), on_update=db.func.current_timestamp())