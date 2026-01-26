#inserting dummy data initially to test our model 
from database import users, links, click_events

# Clear old data
users.delete_many({})
links.delete_many({})
click_events.delete_many({})

# Insert sample user
users.insert_one({
    "user_id": "u123",
    "username": "creator01"
})

# Insert links
links.insert_many([
    {"link_id": "l101", "user_id": "u123", "title": "YouTube", "url": "https://youtube.com/example"},
    {"link_id": "l102", "user_id": "u123", "title": "Instagram", "url": "https://instagram.com/example"},
    {"link_id": "l103", "user_id": "u123", "title": "Merch Store", "url": "https://shop.example.com"}
])

# Insert metadata
click_events.insert_many([
    {"link_id": "l101", "impressions": 1500, "clicks": 180, "peak_time": "19:00-22:00"},
    {"link_id": "l102", "impressions": 1200, "clicks": 96,  "peak_time": "18:00-21:00"},
    {"link_id": "l103", "impressions": 800,  "clicks": 12,  "peak_time": "20:00-23:00"}
])

print("Dummy data inserted successfully.")
