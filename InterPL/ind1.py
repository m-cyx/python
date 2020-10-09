from itertools import permutations


def is_palindrome(word):
    return word == word[::-1]


def get_word():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    symbols = list()
    for num in nums:
        symbols.append((hex(num).upper()[2:len(hex(num))]))
    return ''.join(symbols)


def solution():
    perms = list(permutations(get_word()))
    for elem in perms:
        if is_palindrome(''.join(elem)):
            return 1
    return 0


print(solution())
