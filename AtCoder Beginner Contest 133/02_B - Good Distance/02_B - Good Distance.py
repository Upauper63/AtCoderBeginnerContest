import sys

f = open('02_B - Good Distance.txt', 'r')
sys.stdin = f

import math
N, D = map(int, input().split(' '))
X_ls = []
cnt = 0

for i in range(N):
    X_ls.append(list(map(int, input().split(' '))))

for i in range(N - 1):
    for j in range(i+1, N):
        dist_squared, dist = 0, 0
        for y, z in zip(X_ls[i], X_ls[j]):
            dist_squared += (y - z) ** 2
        dist = math.sqrt(dist_squared)
        if dist - math.floor(dist) == 0:
            cnt += 1
print(cnt)