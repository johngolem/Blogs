from flask_script.commands import Command
from app import create_app,db
from app.models import Comment, Downvote, Upvote, User,Blog
from  flask_migrate import Migrate
from flask_wtf import FlaskForm


# app = create_app('development')
app = create_app('development')




migrate = Migrate(app,db)


@app.shell_context_processor
def make_shell_context():
    return dict( db = db, User =User, Blog=Blog, Upvote=Upvote, Downvote=Downvote,Comment=Comment)


