
import sys
f = open('02_B - Remove It.txt', 'r')
sys.stdin = f

N, X = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
for i in ls:
    if i != X:
        print(i, end=' ')