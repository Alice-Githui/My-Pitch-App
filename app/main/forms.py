from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    comment=TextAreaField('Add Comment', validators=[Required()])
    submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us something about yourself', validators=[Required()])
    submit=SubmitField('Submit')


class PitchForm(FlaskForm):
    category=SelectField('Select Category',choices=[('pickuppitch', 'Pick-Up Lines'), ('technology','Technology'),('business','Business'),('legal', 'Legal'),('inspirational', 'Inspirational'),('others','Other')])
    title=StringField('Title',validators=[Required()])
    description=TextAreaField('Share details about your pitch', validators=[Required()])
    submit=SubmitField('Enter Your Pitch')