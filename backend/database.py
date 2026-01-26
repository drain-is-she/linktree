# this file will enabl us to connect the project with mongodb and we have selected three collections user links and click events 
#user-this will have the user data 
#links - frm where they have been reffered 
#click event - CTR and all thta stuff 
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["linktreeDB"]

users = db["users"]
links = db["links"]
click_events = db["click_events"]
