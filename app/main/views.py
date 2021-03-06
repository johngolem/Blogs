from . import main
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, abort, request
from . forms import BlogForm, CommentForm
from .. models import Blog, User, Comment, Upvote, Downvote
from .. import db
from  ..requests import getQuotes




@main.route('/')
def index():

    getquotes = getQuotes()
    blogs = Blog.query.all()
    lifestyle = Blog.query.filter_by(category='lifestyle').all()
    career = Blog.query.filter_by(category='career').all()
    learning = Blog.query.filter_by(category='learning').all()
    return render_template('index.html', blogs=blogs, lifestyle=lifestyle, career=career, learning=learning, getquotes=getquotes)


@main.route('/create_new', methods=['POST', 'GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_blog_object = Blog(post=post, user_id=current_user._get_current_object(
        ).id, category=category, title=title)
        new_blog_object.save_b()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', form=form)


@main.route('/comment/<int:blog_id>', methods=['POST', 'GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id=blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment, user_id=user_id, blog_id=blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id=blog_id))
    return render_template('comment.html', form=form, blog=blog, all_comments=all_comments)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username=name).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id=user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user, posts=posts)
