
import sys
f = open('03_C - Mandarin Orange.txt', 'r')
sys.stdin = f

n = int(input())
max_val = 0
a_ls = list(map(int, input().split(' ')))
for i in range(n):
    x = a_ls[i]
    max_val = max(max_val, a_ls[i])
    for j in range(i + 1, n):
        if x > a_ls[j]:
            x = a_ls[j]
        max_val = max(max_val, x * (j - i + 1))
print(max_val)            