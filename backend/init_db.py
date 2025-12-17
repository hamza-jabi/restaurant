import sqlite3

conn = sqlite3.connect("restaurants.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    meals TEXT NOT NULL,
    rating REAL NOT NULL
)
""")

cur.execute("DELETE FROM restaurants")

data = [
    ("Al Quds Shawarma", "Nablus", "shawarma,arabic,grill,chicken", 4.8),
    ("Pizza House", "Ramallah", "pizza,italian,pasta", 4.5),
    ("Burger Lab", "Jenin", "burger,fries,fast food", 4.6),
    ("Sushi Spot", "Tulkarm", "sushi,japanese,seafood", 4.4),
    ("Falafel King", "Hebron", "falafel,arabic,vegetarian", 4.7),
]

cur.executemany(
    "INSERT INTO restaurants (name, location, meals, rating) VALUES (?, ?, ?, ?)",
    data
)

conn.commit()
conn.close()
print("DB initialized: restaurants.db")

