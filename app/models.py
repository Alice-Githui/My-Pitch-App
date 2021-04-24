from . import db

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    bio=db.Column(db.String())
    email=db.Column(db.String())
    pitch=db.relationship('Pitch', backref='user', lazy="dynamic")
    
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