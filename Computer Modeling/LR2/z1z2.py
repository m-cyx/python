# 2.1 Найти площадь треугольника
# 2.2 Найти площадь криволинейной трапеции

# Случайно раскидываем точки по прямоугольнику, и находим площадь фигуры по % попадающих в фигуру точек
# У прямоугольника площадь легко почитать
# Допустим попали 500 из 800 точек, а прямоугольник имел площадь 400, тогда:
# 400*(500/800)

import math
import random

import numpy as np
import matplotlib.pyplot as plt
a = 20
b = 40
k = int(input("Введите кол-во точек: "))
#k = 500
x = np.linspace(0, a, a+1)
plt.title("2.1")
plt.grid()


d = dict()
i = 0
while i < k:
    z = len(d)
    d[i] = (random.uniform(0, a), random.uniform(0, b))
    #if len(d) > z:
    i += 1
#print(d)
kol = 0
gpointsx = list()
gpointsy = list()
rpointsx = list()
rpointsy = list()
for point in d.values():
    if 2 * point[0] > point[1]:
        gpointsx.append(point[0])
        gpointsy.append(point[1])
        kol += 1
        #plt.scatter(point[0], point[1], s=10, c="green")
    else:
        rpointsx.append(point[0])
        rpointsy.append(point[1])
        #plt.scatter(point[0], point[1], s=5, c="red")

plt.scatter(gpointsx, gpointsy, s=10, c='green')
plt.scatter(rpointsx, rpointsy, s=10, c='red')

plt.scatter(0, 0, label='Sпрям = ' + str(a*b))
plt.scatter(0, 0, label='В треугольнике ' + str(kol) + ' из ' + str(k))
plt.scatter(0, 0, label='Sтр (приближённо)= ' + str(round(((a*b) / k) * kol, 3)))
plt.scatter(0, 0, label='Sтр = ' + str(round((a*b) / 2, 3)))
plt.plot(x, 2*x)
plt.plot(x, 0*x)
plt.plot([a, a], [0, b])
plt.legend()
plt.show()

plt.title("2.2")
axes = plt.gca()
axes.set_xlim([0, a])
axes.set_ylim([0, b])
sinx = np.linspace(0, a, a**2)
plt.plot(sinx, 10 * np.sin(sinx)+(b/2))

kol = 0
gpointsx = list()
gpointsy = list()
rpointsx = list()
rpointsy = list()
for point in d.values():
    if 10 * np.sin(point[0])+(b/2) > point[1]:
        gpointsx.append(point[0])
        gpointsy.append(point[1])
        kol += 1
        #plt.scatter(point[0], point[1], s=10, c="green")
    else:
        rpointsx.append(point[0])
        rpointsy.append(point[1])
        #plt.scatter(point[0], point[1], s=5, c="red")

plt.scatter(gpointsx, gpointsy, s=10, c='green')
plt.scatter(rpointsx, rpointsy, s=10, c='red')
plt.scatter(0, 0, label='Sпрям = ' + str(a*b))
plt.scatter(0, 0, label='Под синусоидой: ' + str(kol) + ' из ' + str(k))
plt.scatter(0, 0, label='Sсин (приближённо)= ' + str(round(((a*b) / k) * kol, 3)))
plt.scatter(0, 0, label='Sсин = ' + str(811.73))
plt.legend()
plt.grid()
plt.grid()
plt.show()
