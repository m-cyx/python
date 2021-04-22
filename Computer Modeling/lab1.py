import math
import matplotlib.pyplot as plt


def lin(Xi, Yi, n):
    SumX = 0
    SumY = 0
    SumX2 = 0
    SumXY = 0

    for i in range(n):
        SumX += Xi[i]
        SumX2 += Xi[i] * Xi[i]
        SumY += Yi[i]
        SumXY += Xi[i] * Yi[i]

    delta = SumX2 * n - SumX * SumX

    if delta != 0:
        deltaA = round(SumXY * n - SumY * SumX, 4)
        deltaB = round(SumX2 * SumY - SumX * SumXY, 4)

        a = round(deltaA/delta, 2)
        b = round(deltaB/delta, 2)

        e = 0
        for i in range(n):
            e += (Yi[i] - (a * Xi[i] + b)) ** 2

        print('Аппроксимирующая функция: y = ' + str(a) + 'x' + ' + ' + str(b) + '\nS(a,b): {0}\n\n'.format(round(e, 2)))

        yg = []
        for elem in Xi:
            yg.append(a * elem + b)
        global ygl
        ygl = yg
        plt.title("Линейная функция")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.plot(Xi, Yi, color='r', linestyle=' ', marker='o', label='y(x)')
        plt.plot(Xi, yg, label="f(x)")
        plt.legend()
        plt.show()
        plt.close()

def step(Xi, Yi, n):
    lnx = 0
    lnx2 = 0
    lny = 0
    ylnx = 0

    for i in range(n):
        lnx += math.log(Xi[i])
        lnx2 += math.log(Xi[i]) * math.log(Xi[i])
        lny += math.log(Yi[i])
        ylnx += math.log(Yi[i]) * math.log(Xi[i])

    lnx = round(lnx, 4)
    lnx2 = round(lnx2, 4)
    lny = round(lny, 4)
    ylnx = round(ylnx, 4)

    delta = n * lnx2 - (lnx * lnx)

    if delta != 0:
        deltaA = (lny * lnx2) - (ylnx * lnx)
        deltaB = (n * ylnx) - (lny * lnx)

        lna = round(deltaA / delta, 4)
        a = round(math.exp(lna), 2)
        b = round(deltaB / delta, 2)

        e = 0
        for i in range(n):
            e += (Yi[i] - (a * (Xi[i] ** b))) ** 2

        print('Аппроксимирующая функция: y = ' + str(a) + ' * x^' + str(b) + '\nS(a,b): {0}\n\n'.format(round(e, 2)))

        yg = []
        for elem in Xi:
            yg.append(a * (elem ** b))
        global ygs
        ygs = yg

        plt.title("Степенная функция")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.plot(Xi, Yi, color='r', linestyle=' ', marker='o', label='y(x)')
        plt.plot(Xi, yg, label='f(x)')
        plt.legend()
        plt.show()

def exp(Xi, Yi, n):
    lny = 0
    x2 = 0
    xlny = 0
    x = 0

    for i in range(n):
        lny += math.log(Yi[i])
        x += Xi[i]
        x2 += Xi[i] * Xi[i]
        xlny += math.log(Yi[i]) * Xi[i]

    lny = round(lny, 4)
    x2 = round(x2, 4)
    x = round(x, 4)
    xlny = round(xlny, 4)

    delta = n * x2 - (x * x)

    if delta != 0:
        deltaA = (lny * x2) - (xlny * x)
        deltaB = (n * xlny) - (lny * x)

        lna = round(deltaA / delta, 4)
        a = round(math.exp(lna), 2)
        b = round(deltaB / delta, 2)

        e = 0
        for i in range(n):
            e += (Yi[i] - (a * math.exp(Xi[i] * b))) ** 2

        print('Аппроксимирующая функция: y = ' + str(a) + ' * e^(' + str(b) + ' * x)\nS(a,b): {0}\n\n'.format(round(e, 2)))

        yg = []
        for elem in Xi:
            yg.append(a * math.exp(elem * b))
        global yge
        yge = yg
        plt.title("Экспонинцеальная функция")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.plot(Xi, Yi, color='r', linestyle=' ', marker='o', label='y(x)')
        plt.plot(Xi, yg, label='f(x)')
        plt.legend()
        plt.show()

    else:
        print('Система имеет больше одного решения!')

def kvad(Xi, Yi, n):
    x4 = 0
    x3 = 0
    x2 = 0
    x = 0
    x2y = 0
    xy = 0
    y = 0

    for i in range(n):
        x4 += round(Xi[i] ** 4, 4)
        x3 += round(Xi[i] ** 3, 4)
        x2 += round(Xi[i] ** 2, 4)
        x += round(Xi[i], 4)
        x2y += round((Xi[i] ** 2) * Yi[i], 4)
        xy += round(Xi[i] * Yi[i], 4)
        y += round(Yi[i], 4)

    delta = x4 * x2 * n + x3 * x * x2 + x3 * x * x2 - x2 * x2 * x2 - x * x * x4 - x3 * x3 * n

    if delta != 0:
        deltaA = x2y * x2 * n + x3 * x * y + xy * x * x2 - y * x2 * x2 - x * x * x2y - xy * x3 * n
        deltaB = x4 * xy * n + x2y * x * x2 + x3 * y * x2 - x2 * xy * x2 - y * x * x4 - x3 * x2y * n
        deltaC = x4 * x2 * y + x3 * x * x2y + x3 * xy * x2 - x2 * x2 * x2y - x * xy * x4 - x3 * x3 * y

        a = round(deltaA/delta, 2)
        b = round(deltaB / delta, 2)
        c = round(deltaC / delta, 2)

        e = 0
        for i in range(n):
            e += (Yi[i] - (a * (Xi[i] ** 2) + b * Xi[i] + c)) ** 2

        print('Аппроксимирующая функция: y = {0}*x^2 + {1}*x + {2}*c\nS(a,b): {3}\n\n'.format(a, b, c, round(e, 2)))

        yg = []
        for elem in Xi:
            yg.append(a * (elem ** 2) + b * elem + c)
        global ygk
        ygk = yg
        plt.title("Квадратичная функция")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.plot(Xi, Yi, color='r', linestyle=' ', marker='o', label='y(x)')
        plt.plot(Xi, yg, label='f(x)')
        plt.legend()
        plt.show()

def all(Xi, Yi, n):
	global ygl
	global ygs
	global yge
	global ygk
	plt.title("Все функции")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.grid()
	plt.plot(Xi, Yi, color='r', linestyle=' ', marker='o', label='y(x)')
	plt.plot(Xi, ygl, label='Линейная функция')
	plt.plot(Xi, ygs, label='Степенная функиця')
	plt.plot(Xi, yge, label='Экспонинцеальная функция')
	plt.plot(Xi, ygk, label='Квадратичная функция')
	plt.legend()
	plt.show()

    #ygl = []


def main():
    file = open('input.txt', 'r')
    infl = file.read()
    infl = infl.split('\n')
    Xi = infl[0].split(', ')
    Yi = infl[1].split(', ')
    for i in range(len(Xi)):
    	Xi[i] = float(Xi[i])
    for i in range(len(Yi)):
    	Yi[i] = float(Yi[i])   
    n = len(Xi)
    print("Аппроксимировать функцию в виде:\n1. Линейная функция.\n2. Степенная функция.\n3. Экспонинцеальная функция\n4. Квадратичная функция\n5. Выход\n")
    menu = input()
    if menu == "1":
        lin(Xi, Yi, n)
        main()
    elif menu == "2":
        step(Xi, Yi, n)
        main()
    elif menu == "3":
        exp(Xi, Yi, n)
        main()
    elif menu == "4":
        kvad(Xi, Yi, n)
        main()
    elif menu == "5":
        all(Xi, Yi, n)
        main()
    elif menu == "6":
        pass
    else:
        main()


if __name__ == '__main__':
    main()


