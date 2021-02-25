from datetime import datetime
from flask_login import UserMixin
from app import db


post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    created = db.Column(db.String, default=str(
        datetime.now().strftime("%d-%m-%y")))
    raiting = db.Column(db.Integer, default=0)
    tag = db.relationship('Tag', secondary=post_tag,
                          backref=db.backref('tag_post', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('user_post', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        # B: {self.body}; R: {self.raiting};
        return f'ID: {self.id}; T: {self.title}; C: {self.created}; T: {self.tag}; U_ID: {self.user_id}'


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1000))
    created = db.Column(db.String, default=str(
        datetime.now().strftime("%d-%m-%y")))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref(
        'user_comment', lazy='dynamic'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', backref=db.backref(
        'post_comment', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'ID: {self.id}; B: {self.body}; U_ID: {self.user_id}; P_ID: {self.post_id}'


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    nickname = db.Column(db.String(25))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'ID: {self.id}; E: {self.email}; N: {self.nickname}'


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'ID: {self.id}; T: {self.title}'
