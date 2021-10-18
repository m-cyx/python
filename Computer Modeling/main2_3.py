# Вывести погрешность 


import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
pointsCount = 10000
R = 12

def generatePoints(N):
    pointsX = np.random.uniform(0, 1, N) * 2 * R - R
    pointsY = np.random.uniform(0, 1, N) * 2 * R - R
    return (pointsX, pointsY)


def inFigure(pointX, pointY):
    return pointX**2 + pointY**2 <= R**2


points = generatePoints(pointsCount)

theta = np.linspace(0, 2 * np.pi, 100)

xCircle = R * np.cos(theta)
yCircle = R * np.sin(theta)

innerPointsX = list()
innerPointsY = list()
outerPointsX = list()
outerPointsY = list()
kol = 0
for x, y in zip(points[0], points[1]):
    if inFigure(x, y):
        kol += 1
        innerPointsX.append(x)
        innerPointsY.append(y)
    else:
        outerPointsX.append(x)
        outerPointsY.append(y)

innerPointsX = np.array(innerPointsX)
innerPointsY = np.array(innerPointsY)
outerPointsX = np.array(outerPointsX)
outerPointsY = np.array(outerPointsY)

del points

plt.plot(xCircle, yCircle)
plt.scatter(innerPointsX, innerPointsY, s=2, c="green")
plt.scatter(outerPointsX, outerPointsY, s=2, c="red")
plt.axis('scaled')
plt.grid(True)

print(str(kol) + "/" + str(pointsCount))
print("S (приближённо)=" + str((27*24/pointsCount) * kol))
print("S = " + str(math.pi * R**2))
plt.show()
#print(f"Pi (appr): {4 * innerPointsX.size / pointsCount}")
#print(f"Pi (orig): {math.pi}")