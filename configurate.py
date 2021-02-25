from os import getenv


class Configurate(object):
    SECRET_KEY = getenv(key='KEY') or 'KEY'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv(key='DATABASE') or 'sqlite:///post.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 4
