#!C:/Users/Pixel/AppData/Local/Programs/Python/Python38-32/python.exe
import cgi
import html
import io
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
#text1 = text1 + '       testing'  #форматирование

#экранирование строчек
text1 = html.escape(text1)
text2 = html.escape(text2)

# РАБОТАЕТ ЗАПИСЬ В БАЗУ НАДО ПОПРАВИТЬ INDEX HTML ЧТОБЫ НЕ СКРИПТ ИСПОЛНЯЛСЯ НЕ ПОКИДАЯ СТРАНИЦУ
# работаю с базой данных
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO phones
                VALUES ('{}', '{}')""".format(text1, text2)
        )
# Сохраняем изменения
conn.commit()

# дозапись в файл
f = io.open('data.txt', 'a', encoding='utf-8')
f.write(text1 + '\n' + text2 + '\n')

# тут происходит обработка значений, полученных из index.html 
# далее выводится через print html документ с готовым результатом

'''
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Первое поле: {}</p>".format(text1))
print("<p>Второе поле: {}</p>".format(text2))

print("""</body>
        </html>""")
'''

print("Content-type: text/html\n")
print("""
<!DOCTYPE HTML>
<html>
    <head>
        <title>Обработка данных форм</title>
    </head>
    <body>
        <form action="/cgi-bin/form.py">
            <input type="text" name="TEXT_1"> <p>Фирма телефона</p>
            <br>
            <input type="text" name="TEXT_2"> <p>Модель телефона</p>
            <br> <hr>
            <input type="submit" value="Записать в бд">
        </form>
    </body>
</html>
""")