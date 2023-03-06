import sys
f = open('C - Four Variables.txt', 'r')
sys.stdin = f

import math
n = int(input())
ls = [0 for i in range(n)]
cnt = 0
for i in range(1, n):
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if j == i // j:
                ls[i] += 1
            else:
                ls[i] += 2
for i in range(1, n):
    cnt += ls[i] * ls[n - i]
print(cnt)