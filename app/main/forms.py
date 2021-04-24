from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import login_required

class CommentForm(FlaskForm):

    title=StringField('Comment', validators=[Required()])
    comment=TextAreaField('Pitch review', validators=[Required()])
    submit=SubmitField('Submit')