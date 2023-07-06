from pymongo import MongoClient

conn = MongoClient("mongodb+srv://venkateshk:Venkatesh%40417@cluster0.tya28gk.mongodb.net/?retryWrites=true&w=majority")

db = conn["sample_database"]

collection = db["students"]
#mongodb+srv://venkateshk:Venkatesh%40417@cluster0.tya28gk.mongodb.net/