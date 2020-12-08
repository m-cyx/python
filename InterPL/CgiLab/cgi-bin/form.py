#!C:/Users/Pixel/AppData/Local/Programs/Python/Python38-32/python.exe
import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text1 = text1 + '       testing'  #форматирование

text1 = html.escape(text1)
text2 = html.escape(text2)


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