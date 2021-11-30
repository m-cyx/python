"""
Мне надо заносить в бд три солбца переменных,
Читать и считать среднее квадратичное и мат ожидание.

Беру просто .txt файл в котором 3 строки.
В каждой строке разделение по пробелу
"""
import io
import os
import numpy as np
from numpy.core.fromnumeric import mean, std
os.system('cls||clear')

# Ввод и проверка значений
while True:
    zhe = int(input('Железо: '))
    mon = int(input('Монитор: '))
    per = int(input('Периферия: '))
    if (zhe > 10) or (mon > 10) or (per > 10): 
        os.system('cls||clear')
        print('Пожалуйста, введите значения не превышающее 10.')
    else:
        break



# Запись в файл
with open('db.txt', 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('zhe'):
            lines[i] = lines[i].strip() + ' ' + str(zhe) + '\n'
        elif line.startswith('mon'):
            lines[i] = lines[i].strip() + ' ' + str(mon) + '\n'
        elif line.startswith('per'):
            lines[i] = lines[i].strip() + ' ' + str(per) + '\n'
    f.seek(0)
    for line in lines:
        f.write(line)


# Чтение и создание списков, по которым будем считать 
with open('db.txt', 'r+') as f:
    vectors = []
    for eachLine in f:
        lst = eachLine.split()
        lst.remove(lst[0])
        vectors.append(lst)
zhel_vector = list(map(int, vectors[0]))
mon_vector = list(map(int, vectors[1]))
per_vector = list(map(int, vectors[2]))


# Среднее квадратичное по каждому вектору
std_zhel = np.std(zhel_vector)
std_mon = np.std(mon_vector)
std_per = np.std(per_vector)
print('\nCреднее квадратичное по каждому верктору:')
print('По железу: ' + str(std_zhel))
print('По монитору: ' + str(std_mon))
print('По периферии: ' + str(std_per))


# Мат ожидание по каждому вектору
mean_zhel = np.mean(zhel_vector)
mean_mon = np.mean(mon_vector)
mean_per = np.mean(per_vector)
print('\nМат ожидание по каждому вектору:')
print('По железу: ' + str(mean_zhel))
print('По монитору: ' + str(mean_mon))
print('По периферии: ' + str(mean_per))





print('\nСписок железо: ' + str(zhel_vector))
print('Список моник: ' + str(mon_vector))
print('Список периферия: ' + str(per_vector))
