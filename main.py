from app import app
from users import users
from posts import posts
import admin
import view


if __name__ == '__main__':
    app.register_blueprint(blueprint=users, url_prefix='/users')
    app.register_blueprint(blueprint=posts, url_prefix='/posts')
    app.run()
