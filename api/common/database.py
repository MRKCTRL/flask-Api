import pymongo

class  Database(object):
    URI = ''
    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.Uri)
        database.DATABASE = cient['fullstack']



    @staticmethod
    def insert(collection, data):
        Database.DATABASE[colecction].insert(data)


    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)


    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
