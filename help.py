s = ['abcd']
A = ['abcd']

def proverka (s,A):
    for el in s:
        if el not in A:
            return False
    return True

print(proverka(s, A))