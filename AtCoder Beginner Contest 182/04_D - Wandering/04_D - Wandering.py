
import sys
f = open('04_D - Wandering.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
sum_ls = [ [] for i in range(N + 1) ]
max_ls = [ [] for i in range(N + 1) ]
sum_ls[0] = 0
max_ls[0] = 0
for i in range(1, N + 1):
    sum_ls[i] = ls[i - 1] + sum_ls[i - 1]
    max_ls[i] = max(max_ls[i - 1], sum_ls[i])
tmp, rst = 0, 0
for i in range(N + 1):
    rst = max(tmp + max_ls[i], rst)
    tmp += sum_ls[i]
print(rst)