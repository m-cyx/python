"""
Выборы в США - 2
"""
states = {}
listofstates = []
listofcondidat = []
N = int(input('Введите кол-во штатов: '))
for i in range(N):
    s = input('Введите штат и кол-во выборщиков: ')
    s = s.split()
    states [s[0]] = int(s[1])
    listofstates.append(s[0])

print(states) # это словарь, в котором штат : кол-во выборщиков

results = []
tmp = input('штат - избиратель: ')  # тут нужна проверка, что голосует не больше людей, чем в штате выборщиков 
while tmp != '0':
    stmp = tmp.split()
    results.append(stmp)
    listofcondidat.append(stmp[1])
    tmp = input('штат - избиратель: ')
    set(listofcondidat)
print('Результаты голосования: ' + str(results))
list1 = []  # это результаты голосования в каждом штате 
list2 = []

for el in results:
    if el[0] == listofstates[0]:
        list1.append(el)
        
for el in results:
    if el[0] == listofstates[1]:
        list2.append(el)

counter = 0
counter2 = 0

for el in list1:
    if el[1] == listofcondidat[0]:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    print('В первом штате победил первый кандидат')
else:
    print('В первом штате победил второй кандидат')
print('Результаты голосования в первом штате: ' + str(list1))
print('Результаты голосования в втором штате: ' + str(list2))
print('Список кандидатов: ' + str(set(listofcondidat)))
# пройти по списку и если первый элемент в паре равен первому элементу из списка штатов, 
# то добавить эту пару в list1 и тд для кол-ва штатов 

# добавить подсчёт голосов из списка штатов

