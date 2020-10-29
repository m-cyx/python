"""
Выборы в США - 2
"""
states = {}
listofstates = []
N = int(input('Введите кол-во штатов: '))
for i in range(N):
    s = input('Введите штат и кол-во выборщиков: ')
    s = s.split()
    states [s[0]] = int(s[1])
    listofstates.append(s[0])

print(states)

results = []
dresults = {}
tmp = input('штат - избиратель: ')  # тут нужна проверка, что голосует не больше людей, чем в штате выборщиков 
while tmp != '0':
    stmp = tmp.split()
    results.append(stmp)
    dresults [stmp[0]] = stmp[1]
    tmp = input('штат - избиратель: ')
print(results)
print(dresults)
list1 = []
list2 = []
"""
for el in results:
    for el1 in el:
        if el1 == listofstates[0]:
            list1.append(el)
"""
for el in results:
    if el[0] == listofstates[0]:
        list1.append(el)
print(list1)
print(list2)

# пройти по списку и если первый элемент в паре равен первому элементу из списка штатов, 
# то добавить эту пару в list1 и тд для кол-ва штатов 
