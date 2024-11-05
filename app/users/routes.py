from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask_login import login_user, logout_user

from app.users.models import User, SmsCode
from app.users.forms import UserCodeVerifyForm, UserRegistrationForm
from app.extentions import sms_api
from app.extentions import db
from .forms import UserLoginForm

import random
import datetime


blueprint = Blueprint('users', __name__)


@blueprint.route('/register', methods=['post','get'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        rand_num = random.randint(1000, 9999)
        session['phone_number'] = form.phone.data
        params = {'sender':'', 'receptor': int(form.phone.data), 'message': rand_num}
        sms_api.sms_send(params)
        code = SmsCode(number=rand_num, phone=form.phone.data,
                       expire_time=datetime.datetime.now() + datetime.timedelta(minutes=5))
        db.session.add(code)
        db.session.commit()
        return redirect(url_for('users.verify'))
    return render_template('user/register.html', form=form)


@blueprint.route('/verify', methods=['post', 'get'])
def verify():
    user_phone = session.get('phone_number')
    code = SmsCode.query.filter_by(phone=user_phone).first()
    form = UserCodeVerifyForm()
    if form.validate_on_submit():
        if code.expire_time < datetime.datetime.now():
            flash('expiration error , please try again')
            return redirect('users.register')
        if form.code.data != code.number:
            flash('your code is wrong')
        else:
            user = User(phone=user_phone)
            db.session.add(user)
            db.session.commit()
            flash('created account', 'info')
    return render_template('user/verify.html', form=form)


@blueprint.route('/login', methods=['post', 'get'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        login_user(user)
        flash('you logged in')
        return redirect('/')
    return render_template('user/login.html', form=form)


@blueprint.route('/logout', methods=['get', 'post'])
def logout():
    logout_user()
    flash('you logged out')
    return redirect('/')
