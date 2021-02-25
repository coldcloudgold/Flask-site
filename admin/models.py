from flask import abort
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
# from models import Post, Comment, User, Tag


class Adminview(ModelView):
    # column_list =  (
    #     Post.user_id,
    #     Post.title,
    #     Post.body,
    #     Post.created,
    #     Comment.post_id,
    #     Comment.body,
    #     Comment.created,
    #     User.email,
    #     User.nickname,
    #     User.admin,
    #     Tag.title,
    # )
    def is_accessible(self):
        try:
            return current_user.admin
        except:
            return False

    def inaccessible_callback(self, name, **kwargs):
        abort(status=404)


class Homeadminview(AdminIndexView):
    def is_accessible(self):
        try:
            return current_user.admin
        except:
            return False

    def inaccessible_callback(self, name, **kwargs):
        abort(status=404)
