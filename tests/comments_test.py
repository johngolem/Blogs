
import unittest
from app.models import Comment, Blog, User
from app import db

class CommentTest(unittest.TestCase):
    def setUp(self):
        
        self.newComment = Comment(id = 1, comment = 'Test comment', user = self.userJohn, blog_id = self.newBlog)
        
    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
    
    def checkvariablesTest(self):
        self.assertEquals(self.newComment.comment,'Test comment')
        self.assertEquals(self.newComment.user,self.userJohn)
        self.assertEquals(self.newComment.blog_id,self.newBlog)


class CommentTest(unittest.TestCase):
    def setUp(self):
        self.userJohn = User(username='John', password='123', email='jpa@gmail.com')
        self.newBlog = Blog(id=1, title='Hustle', content='Testing', user_id=self.userJohn.id)
        self.newComment = Comment(id=1, comment =' test comment', user_id=self.userJohn.id, blog_id = self.newBlog.id )

    def tearDown(self):
        Blog.query.deleteBlog()
        User.query.deleteUser()
        Comment.query.deleteComment()

    def checkInstanceVariables(self):
        self.assertEquals(self.newComment.comment, 'test comment')
        self.assertEquals(self.newComment.user_id, self.user_John.id)
        self.assertEquals(self.newComment.blog_id, self.new_blog.id)