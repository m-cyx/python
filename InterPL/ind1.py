from itertools import permutations

# палиндром
def is_palindrome(word):
    return word == word[::-1]


def get_word():
    # ввожу n элементов
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    symbols = list()
    # прохожу по списку чисел, вставляю в список символов 16ричные числа (без 0x)
    for num in nums:
        symbols.append((hex(num)[2:len(hex(num))])) #длина 16ричного - 2 префиксных
    # возвращаю список 16ричных цифр
    return ''.join(symbols)


def solution():
    # список всех возможных перестановок 
    perms = list(permutations(get_word()))
    for elem in perms:
        if is_palindrome(''.join(elem)):
            return 1
    return 0


print(solution())
