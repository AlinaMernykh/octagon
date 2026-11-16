from db.db import Base, engine, SessionLocal
from db import crud

# Создаем таблицы
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Создаем категории
cat1 = crud.create_category(db, "Фантастика")
cat2 = crud.create_category(db, "Классика")

# Добавляем книги
crud.create_book(db, "Дюна", "Научная фантастика о пустынной планете", 599.90, "", cat1.id)
crud.create_book(db, "Основание", "Классика научной фантастики", 499.90, "", cat1.id)
crud.create_book(db, "Война и мир", "Роман-эпопея Льва Толстого", 899.90, "", cat2.id)
crud.create_book(db, "Преступление и наказание", "Роман Достоевского", 399.90, "", cat2.id)

db.close()
print("База данных успешно инициализирована!")
