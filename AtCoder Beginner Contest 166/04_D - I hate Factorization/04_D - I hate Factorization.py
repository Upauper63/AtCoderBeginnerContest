
import sys
f = open('04_D - I hate Factorization.txt', 'r')
sys.stdin = f

X = int(input())
for i in range(-1000, 1000):
    for j in range(-1000, 1000):
        if i ** 5 - j ** 5 == X:
            print(i, j)
            exit()