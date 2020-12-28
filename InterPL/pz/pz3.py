# кол-во кубиков 2х
# цвета кубиков 

# вывести все кубики что есть у ребёнка
# вывести все возможные кубики
# вывести все что есть у второго, но нет у первого
# вывести общие цвета 
					
player1 = set(map(str,input("Введите кубики первого: ").split()))
player2 = set(map(str,input("Введите кубики второго: ").split()))

print("Все кубики первого: " + str(player1))
print("Все кубики второго: " + str(player2))
print("Кол-во кубиков у первого: " + str(len(player1)))
print("Кол-во кубиков у второго: " + str(len(player2)))
print("Все возможные цвета: " + str(player1.union(player2)))
print("Есть у первого, но нет у второго: " + str(player1.difference(player2)))
print("Общие цвета: " + str(player1.intersection(player2)))
