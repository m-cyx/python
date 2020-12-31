from __future__ import print_function
import math



# Инициализация алгоритма Флойда-Уоршелла
'''Алгоритм нахождения длин кратчайших путей 
между всеми парами вершин во взвешенном ориентированном графе'''
def floyd(matrix):
    for k in range(len(matrix)):
        for i in range (len(matrix)):
            for j in range (len(matrix)):
                if i == j:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])

# Открываю файл на чтение
f = open('in.txt', encoding = 'utf-8') 

# Указываю количество комнат в бункере
n = int(f.readline()) 

# Инициализирую радиусы действия датчиков звука
action_radius = list(map(int, f.readline().split()))  

#Инициализирую матрицу длин коридоров между комнатами
matrix = [[math.inf for j in range(n)] for i in range(n)] 
for i in range(n-1): 
    edges = list(map(int, f.readline().split())) 
    matrix[edges[0]-1][edges[1]-1] = edges[2] 
    matrix[edges[1]-1][edges[0]-1] = edges[2]
f.close() 

# Инициализирую список степеней вершин 
vertexes_degrees = []
for i in range(len(matrix)): 
    adj = [1 for j in range(len(matrix[i])) if matrix[i][j] < math.inf] 
    vertexes_degrees.append(sum(adj))

# Инициализирую диаметры действия  датчиков звука = vertexes_degrees * action_radius    
action_diameter = [list(range(0, n)), list(map((lambda x, y: x * y), vertexes_degrees, action_radius))] 

# Инициализирую список посещенных вершин 
visited = [False] * n 

# Сортирую номера вершин в порядке убывания диаметров действия датчиков звука
for i in range(n): 
    for j in range(n-i-1): 
        if action_diameter[1][j] < action_diameter[1][j+1]: 
            action_diameter[1][j], action_diameter[1][j+1] = action_diameter[1][j+1], action_diameter[1][j]
            action_diameter[0][j], action_diameter[0][j + 1] = action_diameter[0][j + 1], action_diameter[0][j]

# Инициализирую матрицу кратчайших путей алгоритмом  Флойда-Уоршелла 
floyd(matrix) 

# Формирую список для результата работы
result = [] 
for i in range(n): 
    v = action_diameter[0][i] 
    numbers_of_visited_rooms = [v]
    if not visited[v]: 
        result.append(v) 
        while len(numbers_of_visited_rooms) != 0:
            v = numbers_of_visited_rooms[0]
            visited[v] = True
            for j in range(len(matrix)):
                if matrix[v][j] > 0 and matrix[v][j] <= action_radius[v] and visited[j] == False : 
                    numbers_of_visited_rooms.append(j)
            del numbers_of_visited_rooms[0]

# Вывод результата в консоль            
print(result)

# Запись результата в файл out.txt
f = open('out.txt', 'w', encoding = 'utf-8') 
f.write(str(len(result)))
f.close() 

