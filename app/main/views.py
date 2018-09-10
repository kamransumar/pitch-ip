from flask import render_template
from flask_login import login_required
from . import main


# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title)


@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def new_review(id):
    pass
