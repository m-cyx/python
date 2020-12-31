# Открываю на чтение
f = open('5in.txt', 'r').read().split("\n")
size = f[0].split()
matr = [[0] * (int(size[1])) for i in range(int(size[0]))]

# Инициализирую генерацию матрицы
def matrrrr():
    matr = [[0] * (int(size[1])) for i in range(int(size[0]))]
    for i in range(0, int(size[2])):
        perem = f[i + 1].split()
        matr[int(perem[0]) - 1][int(perem[1]) - 1] = "/"
        # /
    for i in range(0, int(size[3])):
        perem = f[i + int(size[2]) + 1].split()
        matr[int(perem[0]) - 1][int(perem[1]) - 1] = "\\"
        # \
    return matr

# Инициализирую помещение зеркала
def mirrir_enter(a: int, b: int, c: str):
    matr = matrrrr()
    i = 0  
    j = 0  
    direction = 1  # 1 - вправо, 2 - вниз, 3 - влево, 4 - вверх
    matr[a][b] = c

    while -1 < i < int(size[0]) and -1 < j < int(size[1]):
        if matr[i][j] == 0 or matr[i][j] == str(0):
            matr[i][j] = 1
            if direction == 1:
                j += 1
            elif direction == 2:
                i += 1
            elif direction == 3:
                j -= 1
            elif direction == 4:
                i -= 1

        elif matr[i][j] == 1 or matr[i][j] == str(1):
            matr[i][j] = 1
            if direction == 1:
                j += 1
            elif direction == 2:
                i += 1
            elif direction == 3:
                j -= 1
            elif direction == 4:
                i -= 1

        elif matr[i][j] == '/':
            matr[i][j] = 0
            if direction == 1:
                direction = 4
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 2
            elif direction == 4:
                direction = 1

        elif matr[i][j] == '\\':
            matr[i][j] = 0
            if direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 4
            elif direction == 4:
                direction = 3

        if i == int(size[0]) - 1 and j == int(size[1]) - 1 and direction == 1:
            return True

    return False


matr = matrrrr()
mass_of_keys = []

if mirrir_enter(0, 0, "0"):
    fout = open('5out.txt', 'w')
    fout.write("0")
    fout.close()

else:
    for i in range(0, int(size[0])):
        for j in range(0, int(size[1])):
            if mirrir_enter(i, j, "/"):
                mass_of_keys.append(("/", i+1, j+1))
            if mirrir_enter(i, j, "\\"):
                mass_of_keys.append(("\\", i+1, j+1))

    if len(mass_of_keys) == 0:
        fout = open('5out.txt', 'w')
        fout.write("impossible")
        fout.close()

    else:
        x1, x2, x3 = min(mass_of_keys)
        fout = open('5out.txt', 'w')
        fout.write(str(len(mass_of_keys)) + " " + str(x2) + " " + str(x3))
        fout.close()



