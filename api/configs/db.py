import os
from pymongo import MongoClient

dbHost = os.environ.get('DB_HOST')
dbPort = os.environ.get('DB_PORT')
dbName = os.environ.get('DB_NAME')
CONNECTION_STRING = f"mongodb://{dbHost}:{dbPort}"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)

db = client[dbName]

users_collection = db["users_collection"]