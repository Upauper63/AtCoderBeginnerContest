import sys
f = open('03_C - ORXOR.txt', 'r')
sys.stdin = f

n = int(input())
if n == 1:
    rst = input()
    print(rst)
    exit()

ls = list(map(int, input().split(' ')))
rst = float('inf')

for i in range(1 << n):
    tmp = 0
    val = 0
    for j in range(n):
        tmp |=  ls[j]
        if i >> j & 1:
            val ^= tmp
            tmp = 0
    val ^= tmp

    rst = min(val, rst)
print(rst)