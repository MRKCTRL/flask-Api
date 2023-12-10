



class User(object):
    def __init__(self, email, password,_id=None):
        self.email =  email
        self.password = password
        self._id =  uuid.uuid4().hex if _id is none else id



        @classmethod
    def get_by_email(self):
        data = Database.find_one('users', {'email': self.email})
        if data is not None:
            return cls(**data)



    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'_id': _id})
        if data is not None:
            return cls(**data)
        # return None

        @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @staticmethod
    def register(cls, email, password):
        user = user.get_by_email(email)
        if user is None:

            new_user = User(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return FALSE

    @staticmethod
    def login(self):
        session['email'] = user_email


    @staticmethod
    def logout():
        session['email'] = None

    def json(self):
        return {
            'email': self.email,
            'id': self._id,
            'password': self.password
        }

    def new_blog(self, title, description):
    blog = Blog(author=self.email,
                        title=title,
                        author_id=self._id)

    blog.save_to_mongo()

    @staticmethod
    def new_post(title, content, date=datetimte.datetime.utcnow())  :
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title=title,
                    content=content,
                    date=date)



    def save_to_mongo(self):
        Database.insert('users', self.json())


        def get_blogs(self):
            return Blog.find_by_author_idself._id)
