import io

def replace_line(file_name, line_num, text):
    f = io.open(file_name, encoding='utf-8')
    lines = f.readlines()
    lines[line_num] = text
    out = io.open(file_name, 'w', encoding='utf-8')
    out.writelines(lines)
    out.close()
    f.close()



replace_line('page.html', 6, '      <p> Проверка 1 </p>\n') #сделать третий аргумент переменной, которая заранее формируется для 
replace_line('page.html', 7, '      <p> Проверка 2 </p>\n')
replace_line('page.html', 8, '      <p> Проверка 3 </p>\n')



<!DOCTYPE HTML>
<html>
    <head>
        <title>Результаты анализа</title>
    </head>
    <body>
        <p align="center" style="color:#ff0099; font-size:30px; font: 20pt Arial;"> Проверка </p>

    </body>    
</html>


