from flask import render_template, request,redirect, url_for,abort
from .import main
from flask_login import login_required,current_user
from ..models import Pitch, User,Category,Comment
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

        return redirect(url_for('main.new_pitch'))

    return render_template('pitches.html', pitchform=pitchform)

@main.route('/pitch/categories', methods=['GET','POST'])
@login_required
def pitch_categories():
    pitch=Pitch.query.filter_by().first()
    pickuppitch=Pitch.query.filter_by(category="pickuppitch")
    technology=Pitch.query.filter_by(category="technology")
    business=Pitch.query.filter_by(category="business")
    legal=Pitch.query.filter_by(category="legal")
    inspirational=Pitch.query.filter_by(category="inspirational")
    others=Pitch.query.filter_by(category="others")

    return render_template('allpitches.html', pitch=pitch,pickuppitch=pickuppitch,technology=technology,business=business,legal=legal,inspirational=inspirational,others=others)

@main.route('/pickuplines', methods=['GET', 'POST'])
def pickuplines():
    pitch=Pitch.query.filter_by().first()
    pickuppitch=Pitch.query.filter_by(category="pickuppitch")
    return render_template('allpitches.html', pitch=pitch,pickuppitch=pickuppitch)

@main.route('/technology', methods=['GET','POST'])
def technology():
    pitch=Pitch.query.filter_by().first()
    technology=Pitch.query.filter_by(category="technology")
    return render_template('tech.html', pitch=pitch, technology=technology)

@main.route('/business',methods=['GET', 'POST'])
def business():
    pitch=Pitch.query.filter_by().first()
    business=Pitch.query.filter_by(category="business")
    return render_template('business.html', pitch=pitch,business=business)

@main.route('/legal',methods=['GET', 'POST'])
def legal():
    pitch=Pitch.query.filter_by().first()
    legal=Pitch.query.filter_by(category="legal")
    return render_template('legal.html', pitch=pitch,legal=legal)

@main.route('/inspirational',methods=['GET', 'POST'])
def inspirational():
    pitch=Pitch.query.filter_by().first()
    inspirational=Pitch.query.filter_by(category="inspirational")
    return render_template('inspirational.html', pitch=pitch,inspirational=inspirational)

@main.route('/other', methods=['GET', 'POST'])
def other():
    pitch=Pitch.query.filter_by().first()
    others=Pitch.query.filter_by(category="others")
    return render_template('other.html',pitch=pitch,others=others)


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

@main.route('/pitch/comment/<int:pitch_id>', methods=['GET','POST'])
@login_required
def comment(pitch_id):
    commentForm=CommentForm()
    pitch=Pitch.query.get(pitch_id)

    if commentForm.validate_on_submit():
        comment=commentForm.comment.data
        user_id=current_user
        
        new_comment=Comment(comment=comment, user_id=current_user._get_current_object().id)

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.comment',pitch_id=pitch_id))

    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    return render_template('comments.html',commentForm=commentForm,pitch=pitch)

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