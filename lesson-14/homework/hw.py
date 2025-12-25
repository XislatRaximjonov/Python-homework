import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    print("ID:", student["id"])
    print("Ism:", student["name"])
    print("Yosh:", student["age"])
    print("Baho:", student["grade"])
    print("-" * 20)


import requests

API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

print("Shahar:", data["name"])
print("Harorat:", data["main"]["temp"], "°C")
print("Namlik:", data["main"]["humidity"], "%")
print("Ob-havo:", data["weather"][0]["description"])


import json

FILE = "books.json"

def load_books():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books = load_books()
    new_id = max(book["id"] for book in books) + 1
    books.append({"id": new_id, "title": title, "author": author})
    save_books(books)

def update_book(book_id, title):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            book["title"] = title
    save_books(books)

def delete_book(book_id):
    books = load_books()
    books = [b for b in books if b["id"] != book_id]
    save_books(books)

# Misol
add_book("Advanced Python", "Alice")
update_book(1, "Python for Beginners")
delete_book(2)


import requests
import random

API_KEY = "YOUR_API_KEY"

movies_by_genre = {
    "action": ["Mad Max", "Gladiator", "Die Hard"],
    "comedy": ["The Mask", "Superbad", "Home Alone"],
    "drama": ["Forrest Gump", "The Shawshank Redemption"],
}

genre = input("Janr kiriting (action, comedy, drama): ").lower()

if genre in movies_by_genre:
    movie = random.choice(movies_by_genre[genre])
    url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    print("🎬 Film:", data["Title"])
    print("📅 Yil:", data["Year"])
    print("⭐ Reyting:", data["imdbRating"])
    print("📖 Tavsif:", data["Plot"])
else:
    print("Bunday janr yo‘q")
