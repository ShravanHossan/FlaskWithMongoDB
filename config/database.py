from pymongo import MongoClient

_client = MongoClient("mongodb://127.0.0.1:27017") #host uri
_db = _client.mymongodb    #Select the database
todos = _db.todo #Select the collection name
