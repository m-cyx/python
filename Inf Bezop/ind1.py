"""
 Вариант - 1
 Дан файл со словами с циклическим сдвигом - 3.
 КООРДИНАТА, шифр – РДИНАТАКОО. Написать функцию decode, которая восстанавливает зашифрованное слово.
"""
import io #библиотека для кодировки файла
import nltk
from nltk import word_tokenize

# Функция для декода (сдвиг по заданию -3), получает список и шаг сдвига, возвращает лист со сдвигом
# -3 Зашиврофать, 3 Расшифровать
def decode (lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range (steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst

f = io.open('input.txt', encoding='utf-8')
text = f.read()
words = word_tokenize(text)
def read_and_write_to_file (lst):
    dtext = decode(lst, -3) #это шифрованный лист - результат работы decode 
    dtextstr = ''.join(dtext) # '' - разделитель между элементами списка соответственно 
    f1 = io.open('output.txt', 'a', encoding='utf-8')
    f1.write(dtextstr + ' ')
    f1.close

# Прохожу по всем словам из списка слов. Получил слово - преобразовал в список, отдал функции
for i in words:
    read_and_write_to_file(list(i))

f.close()