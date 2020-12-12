'''
Вводятся пары столица - государство, их надо сортировать по государству
'''
# Инициализация
n = int(input('Введите кол-во строк: '))
dict = {}
gos_list = []

# Ввод словаря и списка государств
for i in range(n):
    s = input('Введите столицу и государство: ')
    s = s.split()
    dict [s[0]] = s[1]
    gos_list.append(s[1])

# Сортированный список государств
gos_list = sorted(gos_list) 

# Вывожу исходный словарь
print(dict)   

# Вывод отсортированных пар
for el in gos_list:
    for key in dict:
        if dict[key] == el:
            print(key + ' ' + dict[key])
