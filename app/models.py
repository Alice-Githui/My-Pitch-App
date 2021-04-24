from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    bio=db.Column(db.String())
    email=db.Column(db.String())
    pitch=db.relationship('Pitch', backref='user', lazy="dynamic")
    pass_secure=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User{self.username}'

class Pitch(db.Model):
    __tablename__='pitch'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    pitch=db.Column(db.String())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User{self.title}'