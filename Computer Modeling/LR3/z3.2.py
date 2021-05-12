import matplotlib.pyplot as plt
import numpy as np


# Входные данные
seed = 3729
kern = 5167
testItersNumber = 1000

# 1357 - вырождается
# 7153 - +- нормально идет

# Разбитие числа на цифры
def getDigits(num):
    return [int(i) for i in list(str(num))]

# Одна итерация
def iteration(num):
    numLen = len(str(num))
    strSq = str((int(num) * kern))

    if len(strSq) != 2 * numLen:
        strSq = '0'*(2 * numLen - len(strSq)) + strSq

    # print(strSq)
    sliceN = len(strSq) - numLen
    rndNum = strSq[sliceN // 2 : - sliceN // 2]
    nextNum = strSq[-numLen : ]
    return (int(rndNum) / 10 ** numLen, nextNum)

# Построение таблички из задания
a, b = 0, seed
for i in range(10):
    a, b = iteration(b)
    print(f"{a:<10}{b:<10}")

# Построение вектора со случайными числами
randomVector = []
curNum = seed
for i in range(testItersNumber):
    rnd, curNum = iteration(curNum)
    print((rnd, curNum))
    randomVector.append(rnd)

np.array(randomVector)

# Гистограмма метода

plt.hist(randomVector)
plt.ylabel('Вероятность')
plt.xlabel('Метод произведений')
plt.show()

# Гистограмма нормального распределения (тестовая)

plt.hist(np.random.normal(0.5, 0.25, testItersNumber))
plt.ylabel('Вероятность')
plt.xlabel('Стандартный метод')
plt.show()

# Проверка на переодичность
a, b = iteration(seed)
acc = [seed]
while b not in acc:
    acc.append(b)
    a, b = iteration(b)
print(b)
