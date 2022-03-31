from hashlib import sha3_256
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    jwt_auth = db.Column(db.Boolean, unique=False, nullable=True, default=False)

    @classmethod
    def email_exists(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def id_exists(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def hash_password(self, password):
        #Todo: Set PYTHONHASHSEED environment variable
        return sha3_256(password.encode()).hexdigest()

    @classmethod
    def check_password(cls, password, email):
        database = cls.query.filter_by(email=email).first().password
        password = sha3_256(password.encode()).hexdigest()

        if database == password:
            return True
        else:
            return False

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def read():
        raise NotImplementedError

    def update():
        raise NotImplementedError

    def delete():
        raise NotImplementedError