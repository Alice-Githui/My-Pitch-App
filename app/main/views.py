from flask import render_template, request,redirect, url_for,abort
from .import main
from flask_login import login_required
from ..models import Pitch, User
from .forms import UpdateProfile, CommentForm
from .. import db

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

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user=user)

@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)