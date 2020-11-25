import sqlite3

conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE books (
                        author text, 
                        title text
                    )
               """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO books
                  VALUES ('Ray', '451gradus')"""
               )
 
# Сохраняем изменения
conn.commit()

conn = sqlite3.connect("mydatabase.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()
 
sql = "SELECT * FROM books"
print(cursor.fetchone()) # or use fetchone()