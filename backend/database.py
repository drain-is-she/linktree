from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["linktreeDB"]

users = db["users"]
links = db["links"]
click_events = db["click_events"]
