# Вывести погрешность 
# Посчитать число Pi тоже с погрешностями
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import quad
pointsCount = 10000
R = 12#12
sd = round(R/2.4)

def generatePoints(N):
    pointsX = np.random.uniform(0, 1, N) * 2 * R - R
    pointsY = np.random.uniform(-2*R, 2*R, N)##pointsY = np.random.uniform(0, 1.21, N) * 2 * R - R
    return (pointsX, pointsY)


def inFigure(pointX, pointY):
    return (pointX**2 + pointY**2 <= R**2) or (pointX**2 + (pointY-sd)**2 <= R**2)


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

plt.plot(xCircle, yCircle, c="green")
plt.plot(xCircle, yCircle+sd, c="green")
plt.scatter(innerPointsX, innerPointsY, s=3, c="green")
plt.scatter(outerPointsX, outerPointsY, s=3, c="red")
plt.axis('scaled')
plt.grid(True)
print(str(kol) + "/" + str(pointsCount))
print("S (приближённо)=" + str((27*24/pointsCount) * kol))
F1 = 2 * math.acos((sd**2)/(2*R*sd))
S1 = (R**2 * (F1 - math.sin(F1)))/2
print("S = " + str(S1*2))
plt.show()