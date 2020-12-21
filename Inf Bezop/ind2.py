'''
Программа считывает input.txt следующего формата: в
первой строке находится целое число L (от 1 до 100) – количество слов в списке.
В следующих L строках – список слов, по одному слову в каждой строке. (слово < 20)
В следующей строке – зашифрованное сообщение из не более чем 200 символов.
Список слов не обязательно содержит все слова из сообщения и наоборот. 
Вывести output.txt: расшифрованное сообщение, содержащее максимальное количество слов 
из входного списка (с учетом их повторений в зашифрованном сообщении). 
Если решений несколько, то вывести одно из них.
'''

import io
def shift(lst,steps): # Функция циклического сдвига
    lst = lst[steps:] + lst[:steps]
    return(lst)

f = io.open('input.txt', encoding='utf-8')
text = f.readlines()
text = [line.rstrip() for line in text] #удаляю служебные переносы строк 

L = int(text[0])
message = text[L+1]
text.pop(L+1)   # выкидываю сообщение
text.pop(0)     # выкидываю L - длина списка строк

print(str(L))   # кол-во слов которые могут попадаться в сообщении
print(text)     # слова, кторые могут попадаться в сообщении
print(message)  # зашифрованное цезарем сообщение, сдвиг k - неизвествен.



abc = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ') # можно сдвигать список алфавита на k влево и расшифровать текст по полученному алфавиту, 
                                          # потом проверить, есть ли слова в расшифровке                                        
abc_list = [] #список всех алфавитов
for i in range(27):
    abc = shift(abc, 1)
    abc_list.append(abc)


new_message = []
new_messages = []
for i in range(len(abc_list)):
    for j in range(len(message)):
        new_message.append(abc[abc_list[i].index(message[j])])
    new_messages.append(new_message)
    new_message = []

message_list = []    
for el in new_messages:
    el = ''.join(el)
    el = el.split()
    message_list.append(el)
#print(message_list)

f = io.open('output.txt', 'w', encoding='utf-8')

for i in range(len(message_list)):
    for el in text:
        if el in message_list[i]:
            print(message_list[i])
            f.write(str(message_list[i]))
            break