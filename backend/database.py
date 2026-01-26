# In-memory demo database

users = [
    {"user_id": "u123", "username": "creator01"}
]

links = [
    {"link_id": "l101", "user_id": "u123", "title": "YouTube", "url": "https://youtube.com/example"},
    {"link_id": "l102", "user_id": "u123", "title": "Instagram", "url": "https://instagram.com/example"},
    {"link_id": "l103", "user_id": "u123", "title": "Merch Store", "url": "https://shop.example.com"}
]

click_events = [
    {"link_id": "l101", "impressions": 1500, "clicks": 180, "peak_time": "19:00-22:00"},
    {"link_id": "l102", "impressions": 1200, "clicks": 96,  "peak_time": "18:00-21:00"},
    {"link_id": "l103", "impressions": 800,  "clicks": 12,  "peak_time": "20:00-23:00"}
]
