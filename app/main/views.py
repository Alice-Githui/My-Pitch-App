from flask import render_template
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
def new_review(id):