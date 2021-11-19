class Blog:

    all_blogs=[]

    def __init__(self,title,category):
        self.title=title
        self.category=category


@classmethod
def get_blogs(cls,id):

    response = []

    for blog in cls.all_blogs:
            if blog.user.id == id:
                response.append(blog)

    return response


def save_blog(self):
        Blog.all_blogs.append(self)