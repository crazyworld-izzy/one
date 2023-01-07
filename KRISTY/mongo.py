from typing import Dict, Union

from pymongo import MongoClient

from KRISTY import MONGO_DB_URI

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["KRISTY"]
