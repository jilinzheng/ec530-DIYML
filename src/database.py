"""
MongoDB database running locally.
Collections: users, images, and models.
"""


from pymongo import MongoClient


# https://pymongo.readthedocs.io/en/stable/faq.html#using-pymongo-with-multiprocessing
def mongo_connect():
    client = MongoClient('mongodb://172.31.16.1:27017/', connect=False)
    db = client['diyml_db']
    users = db['users']
    images = db['images']
    models = db['models']
    return users, images, models
