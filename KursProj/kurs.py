import io
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

# Открытие файла на чтение
f = io.open('colors.txt', encoding='utf-8')
text = f.readlines()
colorcode = [] # код цвета
colorname = [] # название цвета        возможно стоит тоже в начлаьную форму привести, чтобы проще искать 
colorbook = {} # код : название
normalcolorname = [] # название цвета в нормальной форме
for line in text:
    if '#' in line:
        colorcode.append(line.lower())
    else:
        colorname.append(line.lower())

colorcode = [line.rstrip() for line in colorcode] # удаляю служебные \n которые появились при f.readlines()
colorname = [line.rstrip() for line in colorname]
# тут привожу имена цветов в нормальную форму
for el in colorname:
    p = morph.parse(el)[0] 
    normalcolorname.append(str(p.normal_form))
colorbook = dict(zip(normalcolorname, colorcode))
print(colorbook)
f.close()
#################################################################################################
# в этой части беру текст, отчищаю от стоп слов и привожу в начальную форму. На выходе должен быть список слов.

# Открытие файла на чтение
f = io.open('text.txt', encoding='utf-8')
text = f.read()

# получение списка слов и стоп слов
words = word_tokenize(text)
stop_words = set(stopwords.words("russian"))
nostop = []
# Иду по словам, если слово не в стоп листе, то добавляю к списку слов
for i in words:
    if i not in stop_words:
        nostop.append(i.lower())
# убираю знаки пунктуации
punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
nostop = [item for item in nostop if item not in punctuation]
#print(nostop)

#########################################################################################################
# тут пробую найти соответствия
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

normalnostop = []
for el in nostop:
    p = morph.parse(el)[0] 
    normalnostop.append(str(p.normal_form))
#print('******************************************************************')
#print(normalnostop)

for key in colorbook:
    if key in normalnostop:
        print(key)