from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    title=StringField('Comment', validators=[Required()])
    comment=TextAreaField('Pitch review', validators=[Required()])
    submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us something about yourself', validators=[Required()])
    submit=SubmitField('Submit')