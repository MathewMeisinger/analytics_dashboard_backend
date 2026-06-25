from pymongo import MongoClient

from app.config.settings import (
    MONGO_URI,
    DATABASE_NAME,
    COLLECTION_NAME,
)

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

call_data_collection = db[COLLECTION_NAME]
user_collection = db["users"]
