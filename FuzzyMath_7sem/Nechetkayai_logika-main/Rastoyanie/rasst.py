import random
from pyswip import Prolog

def randomize():
    rassts = list()
    for cur in range(10):
        rassts.append(random.randint(1, 170))

    vremias = list()
    for cur in range(10):
        vremias.append(random.randint(1, 24))

    transps = list()
    for cur in range(10):
        transps.append(random.randint(1, 60))

    return rassts, vremias, transps

def zapis(l1, l2, l3):
    with open("data.txt", "w") as f:
        for cur in range(len(l1)):
            f.write(str(l1[cur])+" ")
        f.write("\n")

        for cur in range(len(l2)):
            f.write(str(l2[cur])+" ")
        f.write("\n")

        for cur in range(len(l3)):
            f.write(str(l3[cur])+" ")
        f.write("\n")

def read():
    with open("data.txt", "r") as f:
        # rassts = list()
        # vremias = list()
        # transps = list()
        rassts = f.readline().split()
        rassts = list(map(int, rassts))

        vremias = f.readline().split()
        vremias = list(map(int, vremias))

        transps = f.readline().split()
        transps = list(map(int, transps))

    return rassts, vremias, transps

def print_massivs(mas1,mas2,mas3):
    print("Расстояния: ")
    print_massiv(mas1)
    print("Время: ")
    print_massiv(mas2)
    print("Транспорт: ")
    print_massiv(mas3)
    print()

def print_massiv(mas):
    res = list()
    for i in range(len(mas)):
        res.append(str(mas[i]))
    print(" ".join(res))

def calculate_arithmetic(mas):
    s = 0
    for i in range(len(mas)):
        s+=mas[i]
    return s/len(mas)

def calculate_sygma(mas):
    sr_arythm = calculate_arithmetic(mas)
    s=0
    for i in range(len(mas)):
        s+= (mas[i]-sr_arythm)**2

    return (s/len(mas))**(1/2)

def final(fchislo):
    if fchislo < 0:
        return "У вас что-то не так, оно не может быть отрицательным."
    elif fchislo >=0. and fchislo < 0.5:
        return "Своими ногами топай."
    elif fchislo >=1. and fchislo < 1.5:
        return "Воспользуйся машруткой."
    elif fchislo >=2. and fchislo < 2.5:
        return "Едь на машине."
    elif fchislo >=3. and fchislo < 3.5:
        return "Своими ногами топай, а потом садись в общественный."
    elif fchislo >=4. and fchislo < 4.5:
        return "Своими ногами топай, а потом ехай машиной."
    else:
        return "Ехай общественным с персадкой на машину."

def main():
    #l1, l2, l3 = randomize()
    #zapis(l1, l2, l3)
    rassts, vremias, transps = read()
    print_massivs(rassts, vremias, transps)

    arithm_r = round(calculate_arithmetic(rassts),3)
    arithm_v = round(calculate_arithmetic(vremias),3)
    arithm_t = round(calculate_arithmetic(transps),3)

    sygma_r = round(calculate_sygma(rassts),3)
    sygma_v = round(calculate_sygma(vremias),3)
    sygma_t = round(calculate_sygma(transps),3)


    print("Среднее арифметическое расстояний=  " +
            str(arithm_r) +
            "  Среднее квадратическое = " +
            str(sygma_r))

    print("Среднее арифметическое времён =  " +
          str(arithm_v) +
          "  Среднее квадратическое = " +
          str(sygma_v))

    print("Среднее арифметическое транспорта=  " +
          str(arithm_t) +
          "  Среднее квадратическое = " +
          str(sygma_t))


    rasst = int(input("Введите расстояние: "))
    vremia = int(input("Введите время: "))
    transp = int(input("Введите частоту хождения транспорта: "))


    try:
        prolog = Prolog()
        prolog.consult("nechet1.pl")
        for res in prolog.query(
            f"pr({rasst},{vremia},{transp},{arithm_r},{sygma_r},{arithm_v},{sygma_v},{arithm_t},{sygma_t}, Fchislo)."):
                print(final(res['Fchislo']))

        rassts.append(rasst)
        vremias.append(vremia)
        transps.append(transp)

        zapis(rassts, vremias, transps)
    except:
        print("Произошла ошибка")

if __name__ == '__main__':
    main()
