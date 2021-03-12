import sys

f = open('02_B - TAKOYAKI FESTIVAL 2019.txt', 'r')
sys.stdin = f

N = int(input())
D_ls = list(map(int, input().split(' ')))
result = 0
for i in range(N):
    for j in range(i+1, N):
        result += D_ls[i] * D_ls[j]
print(result)
