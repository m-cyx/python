# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)
 
sum = 0
i = 1
N = int(input("enter n: "))
while fib(i) <= N:
    if fib(i) % 2 == 0:
        sum += fib(i)
    i += 1
print("sum is: " + str(sum))