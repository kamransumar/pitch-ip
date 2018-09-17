from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from ..models import User, Pitch, Comment
from .forms import *
from .. import db, photos
# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'
    pitches = Pitch.query.all()

    return render_template('index.html', title=title, pitches=pitches)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username=name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<name>/update', methods=['GET', 'POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.username = form.username.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', name=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<name>/update/pic', methods=['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.image = path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))


@main.route('/pitch/', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():

        content = form.content.data
        title = form.title.data
        category = form.category.data
        # Updated review instance
        new_pitch = Pitch(
            content=content, title=title, category=category)
        db.session.add(new_pitch)
        db.session.commit()
        # save review method
        # new_pitch.save_pitch()
        # return redirect(url_for('.pitch', id=pitch.id))

    return render_template('pitches.html', pitch_form=form)


@main.route('/pitch/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    view category that returns a form to create a new comment
    '''
    form = CommentForm()
    pitch = Pitch.query.filter_by(id=id).first()

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # comment instance
        new_comment = Comment(
            pitch_id=pitch.id, post_comment=comment, title=title, user=current_user)

        # save comment
        new_comment.save_comment()

        return redirect(url_for('.pitches', id=pitch.id))

    title = f'{pitch.title} comment'
    return render_template('newcomment.html', title=title, comment_form=form, pitch=pitch, )


@main.route('/allpitches')
def pitch_list():

    pitches = Pitch.query.all()

    return render_template('pitches.html', pitches=pitches)


@main.route('/onepitch/<int:id>')
def one_pitch(id):

    pitch = Pitch.query.filter_by(id=id).first()
    form = CommentForm()
    pitch = Pitch.query.filter_by(id=id).first()

    if form.validate_on_submit():
        title = form.title.data
        comment_form = form.comment.data

        # comment instance
        new_comment = Comment(
            pitch_id=pitch.id, post_comment=comment_form, title=title, user=current_user)

        # save comment
        new_comment.save_comment()
        db.session.add(new_comment)
        db.session.commit()

    return render_template('viewpitch.html', pitch=pitch, id=id, comment_form=form)
