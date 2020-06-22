#Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?


#def prost(n):
#    d = 2
#    while n % d != 0:
#        d += 1
#    return d == n # возвращает булевское значение

#N = int(input("Введите число: "))
#max = 0
#for i in range(2, N+1):
#    if (N % i == 0):
#        if prost(i):
#            max = i
#print(max)


import math
def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst
r=issimple(600851475143)
print(max(r))