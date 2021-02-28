'''12.	 Найти количество людей, чей балл выше общего среднего балла. Вывести их список.'''
import io
import csv
import pprint

f = io.open('file_12.csv', 'r', encoding='utf-8')

# table[строка][столбец]
table = [row for row in csv.reader(f)]
marks = []
for i in range(1, len(table)-2):
    marks.append(table[i][9])

marks = [float(el.replace(',', '.')) for el in marks]
print(marks)

avg_mark = float(table[len(table)-1][9].replace(',', '.'))
print(avg_mark)

k = 0
for i in range(1, len(table)-2):
    if float(table[i][9].replace(',', '.')) > avg_mark:
        k += 1
        print(table[i][0] + ' ' + table[i][1])

print(str(k) + ' людей, чей балл выше общего среднего балла')
