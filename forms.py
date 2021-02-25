from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
# from wtforms.validators import Email, Length, DataRequired, EqualTo


class DefaulForm(FlaskForm):
    email = StringField()
    password = PasswordField()


class RegistrationForm(DefaulForm):
    nickname = StringField()
    submit = SubmitField(label='Зарегистрироваться')


class LoginForm(DefaulForm):
    remember = BooleanField(label='Запомнить', default=False)
    submit = SubmitField(label='Войти')


class CreatePost(FlaskForm):
    title = TextAreaField()
    body = TextAreaField()
    submit = SubmitField(label='Создать пост')


class CreateComment(FlaskForm):
    body = TextAreaField()
    submit = SubmitField(label='Комментировать')
