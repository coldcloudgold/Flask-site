from flask_admin import Admin
from app import app, db
from models import Post, Comment, User, Tag
from .models import Adminview, Homeadminview


admin = Admin(app=app, url='/', index_view=Homeadminview())
admin.add_view(view=Adminview(model=Post, session=db.session))
admin.add_view(view=Adminview(model=Comment, session=db.session))
admin.add_view(view=Adminview(model=User, session=db.session))
admin.add_view(view=Adminview(model=Tag, session=db.session))
