import datetime


class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.utcnow(), _id=None):
        self._id = uuid.uuid4().hex if _id is none else id
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author  = author
        self.created_date = created_date



        def get posts(self):
            return Post.from_blog(self._id)


        def save_to_mongo(self):
            Database.insert(collection='blogs',
                            data=self.json())

        def json(self):
            return {
            'author': self.author,
            'title':self.title,
            'description':self.description,
            '_id':self._id,
            }


        @classmethod
        def from_mongo(cls, id):
            post_data = Database.find_one(collection='posts',
                                        query={'_id': id})
            return cls(**post_data)
            # blog_id=post_data['blog_id'],
            #             title=post_data['title'],
            #             content=post_data['content'],
            #             author=post_data['author'],
            #             created_date=post_data['create_date'],
            #             _id=post_data['_id'])

        @staticmethod
        def from_blog(id):
