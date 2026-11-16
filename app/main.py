from db.db import SessionLocal
from db import crud

db = SessionLocal()

print("=== Категории ===")
for cat in crud.get_categories(db):
    print(f"ID: {cat.id}, Название: {cat.title}")

print("\n=== Книги ===")
for book in crud.get_books(db):
    print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price}, Категория ID: {book.category_id}")

db.close()
