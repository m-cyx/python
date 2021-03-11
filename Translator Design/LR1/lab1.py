#Требуется написать "сканер" для перевода с ЯП на кодовый язык
# 7 вариант Basic -> Perl
import io
import nltk
from pprint import pprint
from nltk import word_tokenize

# Открытие файла на чтение
f = io.open('input.txt', encoding='utf-8')
text = f.read()

words = word_tokenize(text)

dict_W = {"LIST": 1, "RUN": 2, "REM": 3, "INPUT": 4, "PRINT": 5, 
            "CLS": 6, "LET": 7, "DIM": 8, "DATA": 9, "READ": 10, 
            "GOTO": 11, "IF": 12, "THEN": 13, "FOR": 14, "NEXT": 15, 
            "WHILE": 16, "WEND": 17, "GOSUB": 18, "RETURN": 19, "END": 20, 
            "CHAIN": 21, "OPEN": 22, "CLOSE": 23, "GET": 24, "PUT": 25, 
            "DELETE": 26, "SAVE": 27, "LOAD": 28, "RENUM": 29} # Служебные слова
dict_O = {"+": 1, "*": 2, "<": 3, ">": 4, "=": 5, ":": 6, "<>": 7} # Операции
dict_R = {" ": 1, ",": 2, ";": 3, "(": 4, ")": 5, ".": 6} # Разделители
dict_I = {} # Идентификаторы/переменные
dict_N = {} # Константы / числа
dict_C = {} # Константы / строки
list_out = [] #Лист выходных значений

print(words)

for el in words:
    if el in dict_W:
        list_out.append( "W" + str(dict_W[el]))
    if el in dict_O:
        list_out.append( "O" + str(dict_O[el]))
    if el in dict_R:
        list_out.append( "R" + str(dict_R[el]))
    if (el not in dict_W) and (el not in dict_O) and (el not in dict_R) and (len(el) == 1) and ():
        print("Есть переменная! " + el)

print(list_out)

# Добавить обработчик переменных, констант и строк
# Написать в виде функций