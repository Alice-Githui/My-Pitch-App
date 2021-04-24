from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Our_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('four_ouw_four.html'),404