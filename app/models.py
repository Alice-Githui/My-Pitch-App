from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime  


class User(UserMixin,db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255), index=True)
    bio=db.Column(db.String())
    email=db.Column(db.String(),unique=True,index=True)
    profile_pic_path=db.Column(db.String())
    password_hash=db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    pitch=db.relationship('Pitch', backref='user', lazy="dynamic")
    comment=db.relationship('Comment', backref="user",lazy="dynamic")
    upvote=db.relationship('Upvote', backref='user',lazy="dynamic")
    downvote=db.relationship('Downvote',backref='user',lazy="dynamic")

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
    description=db.Column(db.String())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    category=db.Column(db.String())
    comment=db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvote=db.relationship('Upvote',backref="pitch",lazy="dynamic")
    downvote=db.relationship('Downvote',backref='pitch', lazy='dynamic')

class Category(db.Model):
    __tablename__ ='category'

    id=db.Column(db.Integer,primary_key=True)
    category=db.Column(db.String())

class Comment(db.Model):
    __tablename__='comment'

    all_comments=[]

    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        
        response=[]

        for comment in cls.all_comments:
            if comment.pitch_id == id:
                response.append(comment)

        return response


class Upvote(db.Model):
    __tablename__='upvote'

    id=db.Column(db.Integer,primary_key=True)
    upvote=db.Column(db.Integer())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

class Downvote(db.Model):
    __tablename__='downvote'

    id=db.Column(db.Integer,primary_key=True)
    upvote=db.Column(db.Integer())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    def __repr__(self):
        return f'User{self.title}'