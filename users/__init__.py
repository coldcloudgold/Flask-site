from flask import Blueprint


users = Blueprint(name='users', import_name=__name__, template_folder='templates')

from users import handlers
