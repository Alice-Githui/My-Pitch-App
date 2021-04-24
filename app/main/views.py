from flask import render_template, request,redirect, url_for,abort
from .import main
from flask_login import login_required,current_user
from ..models import Pitch, User
from .forms import UpdateProfile,CommentForm,PitchForm
from .. import db,photos

#Views
@main.route('/')
def index():
    '''
    View root function that returns the index page and its contents
    '''
    title='Home-Welcome to My Pitch App ... Your 60sec start here.'

    return render_template('index.html', title=title)

@main.route('/pitch/new/', methods=['GET','POST'])
@login_required
def new_pitch():
    pitchform=PitchForm()

    if pitchform.validate_on_submit():
        category=pitchform.category.data
        title=pitchform.title.data
        description=pitchform.description.data
        user_id=current_user

        new_pitch=Pitch(category=category, title=title, description=description,user_id=current_user._get_current_object().id)
        
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('pitches.html', pitchform=pitchform)

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

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user=User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))