import matplotlib.pyplot as plt
import numpy as np

seed = 7153
testItersNumber = 1000

# 1357 - вырождается
# 7153 - +- нормально идет

# Разбитие числа на цифры
def getDigits(num):
    return [int(i) for i in list(str(num))]

# Одна итерация
def iteration(num):
    numLen = len(str(num))
    strSq = str(int(num) ** 2)

    if len(strSq) != 2 * numLen:
        strSq = '0'*(2 * numLen - len(strSq)) + strSq

    sliceN = len(strSq) - numLen
    nextNum = strSq[sliceN // 2 : - sliceN // 2]
    return (int(nextNum) / 10 ** numLen, nextNum)

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

plt.hist(randomVector)
plt.ylabel('Количество')
plt.xlabel('Метод квадратов')
plt.show()

plt.hist(np.random.normal(0.5, 0.25, testItersNumber))
plt.ylabel('Количество')
plt.xlabel('Метод квадратов')
plt.show()

# Проверка на переодичность
a, b = iteration(seed)
acc = [seed]
while b not in acc:
    acc.append(b)
    a, b = iteration(b)
print(b)