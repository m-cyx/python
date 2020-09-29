# Вариант - 1
# Дан файл со словами с циклическим сдвигом - 3.
# КООРДИНАТА, шифр – РДИНАТАКОО. Написать функцию decode, которая восстанавливает зашифрованное слово.

import io #библиотека для кодировки файла
import nltk
from nltk import word_tokenize

# Функция для декода (сдвиг по заданию -3)
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
text1 = f.read()
text = list(f.read())
words = word_tokenize(text1)


print(text)
decodedtext = decode(text,-3)
print(decodedtext)
decodedtextstring = ''.join(decodedtext) # '' - разделитель между элементами списка соответственно
print(decodedtextstring)

f = io.open('output.txt', 'w', encoding='utf-8')
f.write(decodedtextstring)
for i in words:
    f.write(decode(i,-3))

f.close