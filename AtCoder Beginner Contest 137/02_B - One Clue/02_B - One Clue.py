import sys

f = open('02_B - One Clue.txt', 'r')
sys.stdin = f

K, X = map(int, input().split(' '))

for i in range(X-K+1, K+X):
    print(i, end=' ')