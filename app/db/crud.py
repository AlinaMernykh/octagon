from sqlalchemy.orm import Session
from .models import Category, Book

def create_category(db: Session, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    book = Book(title=title, description=description, price=price, url=url, category_id=category_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_categories(db: Session):
    return db.query(Category).all()

def get_books(db: Session):
    return db.query(Book).all()

def get_books_by_category(db: Session, category_id: int):
    return db.query(Book).filter(Book.category_id == category_id).all()

def update_book_price(db: Session, book_id: int, new_price: float):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.price = new_price
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book
