
# import pymongo

# uri="mongodb://127.0.0.1:27017"
# client=pymongo.MongoClient(uri)
# database=client['flask']
# collection=database['students']
# students=collection.find({})
# for student in students:
#     print(student)
from database import Database
from models.post import Post
from models.blog import Blog
from menu import Menu
Database.initialize()

menu=Menu()
menu.run_menu()