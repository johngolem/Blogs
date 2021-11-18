
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('lifestyle', 'lifestyle'), (
        'career', 'career'), ('learning', 'learning')], validators=[Required()])
    post = TextAreaField('Your Blog', validators=[Required()])
    submit = SubmitField('Blog')


class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Comment')


class UpdateBlogs(FlaskForm):
    pass
