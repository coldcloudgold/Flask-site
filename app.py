from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from configurate import Configurate


app = Flask(__name__)
app.config.from_object(Configurate)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)
login_manager = LoginManager(app=app)
# login_manager.login_view('autorization')
