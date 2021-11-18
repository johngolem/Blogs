
from flask_login import login_required
from . import main
from flask import render_template, redirect, url_for,abort,request

@main.route('/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, pitch = blog,all_comments=all_comments)