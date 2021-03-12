
import sys
f = open('03_C - Typical Stairs.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
ls = [ [] for i in range(N + 1) ]
ls[0] = 1
ls[1] = 1
for i in range(M):
    ls[int(input())] = 0
for i in range(2, N + 1):
    if ls[i] != 0:
        ls[i] = ls[i - 2] + ls[i - 1]
print(ls[-1] % 1000000007)