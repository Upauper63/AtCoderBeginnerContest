import os
import sys
f = open('03.txt', 'r')
sys.stdin = f

N = 2 ** int(input())
ls = list(map(int, input().split(' ')))
p1 = max(ls[: N // 2])
p2 = max(ls[N // 2:])
rst = min(p1, p2)
print(ls.index(rst) + 1)