result = [['первый', 1], ['второй', 2], ['третий', 3], ['четвёртый', 4],
            ['первый', 11], ['второй', 22], ['третий', 33], ['четвёртый', 44]]
"""
result2 = ['первый', 'второй', 'третий', 'четвёртый']
for i in range(len(result2)-1):
        print(result2[i])
        print(result2[i+1])
"""
print(result)

listtmp = result
t = int(0) 
for i in range(len(listtmp)-1):
    if listtmp[i] != listtmp[i+1]:
        listtmp.remove(listtmp[i+1])
    #t += 1

print(listtmp)