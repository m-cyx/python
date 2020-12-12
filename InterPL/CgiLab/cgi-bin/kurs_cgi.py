#!C:/Users/Pixel/AppData/Local/Programs/Python/Python38-32/python.exe
import cgi
import html
import io
import sqlite3
import io
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
f = io.open('text.txt', encoding='utf-8')
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


# с помощю cgi попробовать напечатать цветной текст в HTML











'''
можно выводить результат в html с цветами
или в tkinter


рекомендовать последовательность чтения книг 
по нарастанию позитианой тональности и спектрограммы 
связать настрой человека с цветовой гаммой 

переход от спектрограммы к анализу тональности текста 


спич ту текст и цвет 

'''
