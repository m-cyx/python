"""
Выборы в США - 2
"""
states = {}
N = int(input('Введите кол-во штатов: '))
for i in range(N):
    s = input('Введите штат и кол-во выборщиков: ')
    s = s.split()
    states [s[0]] = int(s[1])

print(states)

results = {}
counter = 0
while counter < 4:
    r = input('штат - избиратель: ')
    r.split()
    results [r[0]] = r[1]
    counter += 1
print (results)