from users import users
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from models import Post, User
from app import db


@users.route('/')
@login_required
def profile():
    posts = Post.query.filter_by(user=current_user)
    return render_template(template_name_or_list='users/profile.html', posts=posts)


@users.route('/<nickname>')
def profile_user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == current_user or user is None:
        return redirect(location=url_for(endpoint='users.profile'))
    posts = Post.query.filter_by(user=user)
    return render_template(template_name_or_list='users/profile.html', posts=posts, user=user)


@users.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(location=url_for(endpoint='users.profile'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user_email = User.query.filter_by(email=form.email.data).first()
        user_nickname = User.query.filter_by(
            nickname=form.nickname.data).first()
        if not (user_email and user_nickname):
            new_user = User(email=form.email.data, nickname=form.nickname.data,
                            password=generate_password_hash(form.password.data))
            db.session.add(new_user)
            db.session.commit()
            return redirect(location=url_for(endpoint='users.authorization'))
        flash('Пользователь с такими данными уже существует')
        return render_template(template_name_or_list='users/registration.html', form=form)
    return render_template(template_name_or_list='users/registration.html', form=form)


@users.route('/authorization', methods=['GET', 'POST'])
def authorization():
    if current_user.is_authenticated:
        return redirect(location=url_for(endpoint='users.profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(pwhash=user.password, password=form.password.data):
                login_user(user=user, remember=form.remember.data)
                return redirect(location=url_for(endpoint='index'))
        flash('Данные введены не правильно')
        return render_template(template_name_or_list='users/authorization.html', form=form)
    return render_template(template_name_or_list='users/authorization.html', form=form)


@users.route('/unauthorization')
@login_required
def unauthorization():
    logout_user()
    return redirect(location=url_for(endpoint='index'))
