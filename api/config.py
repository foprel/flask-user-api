import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Development:
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'databases/api.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='abc'