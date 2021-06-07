import sys
f = open('02_B - AtCoder Condominium.txt', 'r')
sys.stdin = f

n, k = map(int, input().split(' '))
rst = 0
for i in range(n):
    for j in range(k):
        rst += 100 * (i + 1) + (j + 1)
print(rst)