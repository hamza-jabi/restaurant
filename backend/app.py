from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("data/restaurants.db")

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/recommend")
def recommend():
    meal = (request.form.get("meal") or "").strip().lower()

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, location, meals, rating
        FROM restaurants
        WHERE lower(meals) LIKE ?
        ORDER BY rating DESC
        LIMIT 1
    """, (f"%{meal}%",))

    row = cur.fetchone()

    if row is None:
        cur.execute("""
            SELECT name, location, meals, rating
            FROM restaurants
            ORDER BY rating DESC
            LIMIT 1
        """)
        row = cur.fetchone()
        matched = False
    else:
        matched = True

    conn.close()

    result = {
        "meal": meal,
        "matched": matched,
        "name": row[0],
        "location": row[1],
        "meals": row[2],
        "rating": row[3],
    }
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
