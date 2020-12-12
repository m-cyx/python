n = int(input('Введите кол-во строк: '))
dict = {}
d_list = []
for i in range(n):
    s = input('Введите столицу и государство: ')
    s = s.split()
    dict [s[1]] = s[0]
    d_list.append(s)

print(dict)
print(d_list) # пары столица - государство, их надо сортировать по государству
