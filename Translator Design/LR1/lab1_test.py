import math

alph = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
all_oper = ' ', ',', ';', '.', '+', '-', '*', '/', '^', '=',  '=', '(', ')', '<', '>', '<>'
rasdel = ' ', ',', ';'
dot = '.'
oper =  '+', '-', '*', '/', '^', '=', '=', '(', ')', '>'
operdouble = '<>', '<'
cifri = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

W = {0: 'W', 1: 'DIM', 2: 'goto', 3: 'GOSUB', 4: 'RETURN',
     5: 'STOP', 6: 'END', 7: 'IF', 8: 'THEN',
     9: 'ELSE', 10: 'REM'}
I = {0: 'I'}
O = {0: 'O', 1: '+', 2: '-', 3: '*', 4: '/', 5: '^',
     6: '<', 7: '>', 8: '=', 9: '<>', 10: '<=',
     11: '>='}
R = {0: 'R', 1: ' ', 2: ',', 3: ';', 4: '(', 5: ')', 6: '.'}
N = {0: 'N'}
C = {0: 'C'}
dict_for_search = [W, O, R]


def my_print(elem1, elem2):
     print(elem1, end='(')
     print(elem2, end='),')


def key_by_value(value, d:dict):
     for elem in d.keys():
          if d[elem] == value:
               return elem


def final_end():
     print(mass_of_words)
     exit(0)
# Сканирование входных данных из файла
f = open('basicinput.txt', 'r')
basic_text = f.read()
basic = basic_text#.split(';\n')

def sem_proc1(word, ind, mass_of_words):
     if word in W.values():
          mass_of_words.append('W' + str(key_by_value(word, W)))
     else:
          ind_I = int(max(I.keys()))
          I[ind_I+1] = (str(word))
          mass_of_words.append('I' + str(ind_I + 1))
     #mass_of_words

     print('proc1: !'+word+'!')
     brench(ind, mass_of_words)
def sem_proc2(word, ind, mass_of_words):
     if word in W.values():
          mass_of_words.append('W' + str(key_by_value(word, W)))
     else:
          ind_I = int(max(I.keys()))
          I[ind_I+1] = (str(word))
          mass_of_words.append('I' + str(ind_I + 1))
     print('proc2: !'+word+'!')
     brench(ind, mass_of_words)
def sem_proc3(word, ind, mass_of_words):
     ind_I = int(max(C.keys()))
     C[ind_I + 1] = (str(word))
     mass_of_words.append('C' + str(ind_I + 1))

     print('proc3: !'+word+'!')
     brench(ind, mass_of_words)
def sem_proc4(word, ind, mass_of_words):
     print('proc4: !'+word+'!')
     if (ind + 1) < len(basic):
          brench(ind + 1, mass_of_words)
     else:
          final_end()
def sem_proc5(word, ind, mass_of_words):
     print('proc5: !'+str(word)+'!')
     if (ind + 1) < len(basic):
          brench(ind + 1, mass_of_words)
     else:
          final_end()
def sem_proc6(word, ind, mass_of_words):
     print('proc6: !'+word+'!')
     if (ind + 1) < len(basic):
          brench(ind + 1, mass_of_words)
     else:
          final_end()
def sem_proc7(word, ind, mass_of_words):
     print('proc7: !'+word+'!')
     if (ind + 1) < len(basic):
          brench(ind + 1, mass_of_words)
     else:
          final_end()
def sem_proc8(word, ind, mass_of_words):
     print('proc8: !'+word+'! ind:'+str(ind))
     if (ind + 1) <  len(basic):
          brench(ind+1, mass_of_words)
     else:
          final_end()
def sem_proc9(word, ind, mass_of_words):
     print('proc9: !'+word+'! ind:'+str(ind))
     if (ind + 1) <  len(basic):
          brench(ind+1, mass_of_words)
     else:
          final_end()
def brench(ind, mass_of_words):
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
                    sem_proc1(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц1
          elif basic[ind] in rasdel:
               sem_proc2(word, ind, mass_of_words)#Если разделитель/операция, то сем.проц2
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
               sem_proc3(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц3
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
                    sem_proc3(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц3
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
                    sem_proc3(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц3
          if basic[ind] in rasdel:
               sem_proc9(word, ind, mass_of_words)  # Если разделитель/операция, то сем.проц9
     if basic[ind] == "\n":
          sem_proc5('\n', ind+1, mass_of_words)
     if basic[ind] in oper:
          sem_proc6(basic[ind], ind, mass_of_words)  # Если операция, то сем.проц6
     if basic[ind] in rasdel:
          sem_proc4(basic[ind], ind, mass_of_words)#Если разделитель/операция, то сем.проц4
     if basic[ind] == '<':
          ind += 1
          if basic[ind] == '>':
               sem_proc7(basic[ind], ind, mass_of_words)  # Если <>, то сем.проц7
          else:
               sem_proc8(basic[ind], ind, mass_of_words)
     final_end()




mass_of_words = list()
ind = 0
maxind = len(basic)
brench(0, mass_of_words)
