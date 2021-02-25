from flask import Blueprint


posts = Blueprint(name='posts', import_name=__name__, template_folder='templates')

from posts import handlers
