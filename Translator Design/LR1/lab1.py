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
def semanticheskaya_procedura1(word, ind, mass_of_words):
     if word in W.values():
          mass_of_words.append('W' + str(key_by_value(word, W)))
     else:
          ind_I = int(max(I.keys()))
          I[ind_I+1] = (str(word))
          mass_of_words.append('I' + str(ind_I + 1))
     #mass_of_words

     print('proc1: !'+word+'!')
     automat(ind, mass_of_words)
def semanticheskaya_procedura2(word, ind, mass_of_words):
     if word in W.values():
          mass_of_words.append('W' + str(key_by_value(word, W)))
     else:
          ind_I = int(max(I.keys()))
          I[ind_I+1] = (str(word))
          mass_of_words.append('I' + str(ind_I + 1))
     print('proc2: !'+word+'!')
     automat(ind, mass_of_words)
def semanticheskaya_procedura3(word, ind, mass_of_words):
     ind_I = int(max(C.keys()))
     C[ind_I + 1] = (str(word))
     mass_of_words.append('C' + str(ind_I + 1))

     print('proc3: !'+word+'!')
     automat(ind, mass_of_words)
def semanticheskaya_procedura4(word, ind, mass_of_words):
     print('proc4: !'+word+'!')
     if (ind + 1) < len(basic):
          automat(ind + 1, mass_of_words)
     else:
          final_end()
def semanticheskaya_procedura5(word, ind, mass_of_words):
     print('proc5: !'+str(word)+'!')
     if (ind + 1) < len(basic):
          automat(ind + 1, mass_of_words)
     else:
          final_end()
def semanticheskaya_procedura6(word, ind, mass_of_words):
     print('proc6: !'+word+'!')
     if (ind + 1) < len(basic):
          automat(ind + 1, mass_of_words)
     else:
          final_end()
def semanticheskaya_procedura7(word, ind, mass_of_words):
     print('proc7: !'+word+'!')
     if (ind + 1) < len(basic):
          automat(ind + 1, mass_of_words)
     else:
          final_end()
def semanticheskaya_procedura8(word, ind, mass_of_words):
     print('proc8: !'+word+'! ind:'+str(ind))
     if (ind + 1) <  len(basic):
          automat(ind+1, mass_of_words)
     else:
          final_end()
def semanticheskaya_procedura9(word, ind, mass_of_words):
     print('proc9: !'+word+'! ind:'+str(ind))
     if (ind + 1) <  len(basic):
          automat(ind+1, mass_of_words)
     else:
          final_end()
def automat(ind, mass_of_words):
     word = ''
     if basic[ind] in alph:
          prov = True
          word += basic[ind]
          ind += 1
          while prov:
               if basic[ind] in alph:
                    word += basic[ind]
                    ind += 1
               else:
                    prov = False
          if basic[ind] in cifri:#Если цифра, то идем дальше.
               prov = True
               word += basic[ind]
               ind += 1
               while prov:
                    if basic[ind] in alph or basic[ind] in cifri:
                         word += basic[ind]
                         ind += 1
                    else:
                         prov = False
               if basic[ind] in rasdel:
                    semanticheskaya_procedura1(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц1
          elif basic[ind] in rasdel:
               semanticheskaya_procedura2(word, ind, mass_of_words)#Если разделитель/операция, то сем.проц2
     if basic[ind] in cifri:
          prov = True
          word += basic[ind]
          ind += 1
          while prov:
               if basic[ind] in cifri:
                    word += basic[ind]
                    ind += 1
               else:
                    prov = False
          if basic[ind] in rasdel:
               semanticheskaya_procedura3(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц3
          elif basic[ind] == '.':
               prov = True
               word += basic[ind]
               ind += 1
               while prov:
                    if basic[ind] in cifri:
                         word += basic[ind]
                         ind += 1
                    else:
                         prov = False
               if basic[ind] in rasdel:
                    semanticheskaya_procedura3(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц3
     if basic[ind] == '.':
          word += basic[ind]
          ind += 1
          if basic[ind] in cifri:
               prov = True
               word += basic[ind]
               ind += 1
               while prov:
                    if basic[ind] in cifri:
                         word += basic[ind]
                         ind += 1
                    else:
                         prov = False
               if basic[ind] in rasdel:
                    semanticheskaya_procedura3(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц3
          if basic[ind] in rasdel:
               semanticheskaya_procedura9(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц9
     if basic[ind] == "\n":
          semanticheskaya_procedura5('\n', ind+1, mass_of_words)
     if basic[ind] in oper:
          semanticheskaya_procedura6(basic[ind], ind, mass_of_words)  # Если операция, то сем.проц6
     if basic[ind] in rasdel:
          semanticheskaya_procedura4(basic[ind], ind, mass_of_words)#Если разделитель/операция, то сем.проц4
     if basic[ind] == '<':
          ind += 1
          if basic[ind] == '>':
               semanticheskaya_procedura7(basic[ind], ind, mass_of_words)  # Если <>, то сем.проц7
          else:
               semanticheskaya_procedura8(basic[ind], ind, mass_of_words)
     final_end()


for el in words:
    if el in dict_W:
        list_out.append( "W" + str(dict_W[el]))
    if el in dict_O:
        list_out.append( "O" + str(dict_O[el]))
    if el in dict_R:
        list_out.append( "R" + str(dict_R[el]))
    if (el not in dict_W) and (el not in dict_O) and (el not in dict_R) and (len(el) == 1) and ():
        print("Есть переменная! " + el)

print(['W4' ,'I1','W12' ,'I1','O4','W13' ,'W5','C1','O6','W11' ,'N1','W5','C2','W4','I2','W5','I2','W20'])
#print(list_out) Выходная строка

# Добавить обработчик переменных, констант и строк
# Написать в виде функций

