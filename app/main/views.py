from flask import render_template, redirect, url_for
from .import main
from flask_login import login_required

#Views
@main.route('/')
def index():
    '''
    View root function that returns the index page and its contents
    '''
    title='Home-Welcome to My Pitch App ... Your 60sec start here.'

    return render_template('index.html', title=title)

@main.route('/pitch/review/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form=CommentForm()
    pitch=get_pitch(id)

    if form.validate_on_submit():
        title=form.title.data
        comment=form.review.data
        new_comment=Comment(comment.id,title,description)
        new_comment.save_comment()
        return redirect(url_for('pitch', id=pitch.id))

    title = f'{pitch.title} review'
    return render_template('new_comment.html', title=title, comment_form=form, pitch=pitch)