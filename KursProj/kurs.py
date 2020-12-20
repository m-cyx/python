import io
import os
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords
import pymorphy2
from collections import Counter
morph = pymorphy2.MorphAnalyzer()


# Открытие файла на чтение
f = io.open('colors.txt', encoding='utf-8')
text = f.readlines()

# Инициализация переменных
colorcode = []          # код цвета
colorname = []          # название цвета
normalcolorname = []    # название цвета в нормальной форме

# Создание словаря цветов из файла colors
for line in text:
    if '#' in line:
        colorcode.append(line.lower())
    else:
        colorname.append(line.lower())

# удаляю служебные \n которые появились при f.readlines()
colorcode = [line.rstrip() for line in colorcode]
colorname = [line.rstrip() for line in colorname]

# Привожу имена цветов в нормальную форму
for el in colorname:
    p = morph.parse(el)[0]
    normalcolorname.append(str(p.normal_form))

# "Упаковываю" названия и цвета в словарь
colorbook = dict(zip(normalcolorname, colorcode))
# print(colorbook)
f.close()

#################################################################################################
# В этой части беру текст, отчищаю от стоп слов и привожу в начальную форму. На выходе должен быть список слов.

# Открытие файла на чтение
f = io.open('text4.txt', encoding='utf-8')
text = f.read()

# Получение списка слов и стоп слов
words = word_tokenize(text)
stop_words = set(stopwords.words("russian"))
nostop = []

# Иду по словам, если слово не в стоп листе, то добавляю к списку слов
for i in words:
    if i not in stop_words:
        nostop.append(i.lower())

# Убираю знаки пунктуации
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
nostop = [item for item in nostop if item not in punctuation]
# print(nostop)

# Инициализирую молфологический анализатор
morph = pymorphy2.MorphAnalyzer()

# Привожу слова из списка без стоп слов в нормальную форму
normalnostop = []
for el in nostop:
    p = morph.parse(el)[0]
    normalnostop.append(str(p.normal_form))
# print(normalnostop)

###################################################################################################

# Собираю список для вывода
out_color = []
for el in normalnostop:
    if el in colorbook:
        out_color.append(el)

# Получаю словарь цвет : кол-во
dict_out_color = Counter(out_color)

# Вывод в консоль
for el in dict_out_color:
    print(el + ' ' + str(dict_out_color[el]) + ' ' + colorbook[el])



# ПОДГОТОВИТЬ СПИСОК СТРОК ДЛЯ ВЫВОДА И В АРГУМЕНТЕ ФУНКЦИИ ОБРАЩАТЬСЯ К СТРОКЕ ИЗ СПИСКА ПО НОМЕРУ
html_string = []
for el in dict_out_color:
    html_string.append('        <p align="center" style="color:{}; font-size:50px; text-shadow: 0px 0px 3px rgba(0, 0, 0, 0.5); font: 20pt Arial;"><strong> {} {} код: {} </strong></p>\n'.format(colorbook[el], el, dict_out_color[el], colorbook[el]))

#print(html_string)

#html_cnt = int(7)
#for el in html_string:
#    replace_line('page.html', html_cnt, el)
#    html_cnt += 1

#вместо того чтобы долбиться в ошибку аут оф рейндж я лучше буду прочто дописывать строки в файл а потом дописать все закрывающие теги 
os.system(r'nul>page.html')
f = io.open('page.html', 'a', encoding='utf-8')
# Записываю открывающие теги
f.write('<!DOCTYPE HTML>\n<html>\n  <head>\n        <title>Результаты анализа</title>\n    </head>\n    <body background="yellow-paper.jpg">\n')

# Записываю результаты работы
for el in html_string:
    f.write(el)

# Закрываю теги 
f.write('    </body>\n</html>')
f.close


#МОЖНО НАЖАТЬ НА КАЖДЫЙ ЦВЕТ И ПОЛУЧИТЬ ЗНАЧЕНИЕ ЕГО СМЫСЛА В ГУГЛЕ ЧЕРЕЗ HREF


'''
можно выводить результат в html с цветами
или в tkinter


рекомендовать последовательность чтения книг 
по нарастанию позитианой тональности и спектрограммы 
связать настрой человека с цветовой гаммой 

переход от спектрограммы к анализу тональности текста 


спич ту текст и цвет 

'''
