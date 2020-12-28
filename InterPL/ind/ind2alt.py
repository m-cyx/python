'''
Дан файл, каждая строка которого может содержать одно или несколько целых чисел, разделенных одним или несколькими пробелами.
Вычислите сумму чисел в каждой строке и выведите эти суммы через пробел (для каждой строки выводится сумма чисел в этой строке).
'''
import io

# Открытие файла на чтение
f = io.open('input.txt', encoding='utf-8')

text = f.readlines()
for line in text:
    splitline = line.split()
    result = sum([int(el) for el in splitline])
    print(result)

f.close