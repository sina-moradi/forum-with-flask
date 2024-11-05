from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError

from app.users.models import User, SmsCode


class UserRegistrationForm(FlaskForm):
    phone = StringField('phone')

    def validate_phone(self, phone):
        codes = SmsCode.query.filter_by(phone=phone.data)
        if codes:
            SmsCode.query.filter_by(phone=phone.data).delete()
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('this user is exists')


class UserCodeVerifyForm(FlaskForm):
    code = StringField('code')


class UserLoginForm(FlaskForm):
    phone = StringField('phone')
