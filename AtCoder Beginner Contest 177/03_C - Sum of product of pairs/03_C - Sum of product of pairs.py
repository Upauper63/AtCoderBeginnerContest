
import sys
f = open('03_C - Sum of product of pairs.txt', 'r')
sys.stdin = f

N = int(input())
rst = 0
ls = list(map(int, input().split(' ')))
extra = 0
for i in ls:
    extra += i ** 2
print((sum(ls) ** 2 - extra) // 2 % (10 ** 9 + 7))