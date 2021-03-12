import sys

f = open('02_B - Multiplication 2.txt', 'r')
sys.stdin = f

input()
ls = list(map(int, input().split(' ')))

if ls.count(0) > 0:
    result = 0
else:
    result = 1
    for i in ls:
        result *= i
        if result > 10 ** 18:
            result = -1
            break
print(result)