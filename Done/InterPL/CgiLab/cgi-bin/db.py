import sqlite3

conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE phones
                  ( Company text, 
                    Model text)
               """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO phones
                  VALUES ('samsung', 'galaxy')"""
               )
 
# Сохраняем изменения
conn.commit()
 
'''
# Вставляем множество данных в таблицу используя безопасный метод "?"
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
 
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
'''