import sys
f = open('04_D - Brick Break.txt', 'r')
sys.stdin = f

n = int(input())
ls = list(map(int, input().split(' ')))
rst, idx = 0, 1
for i in ls:
    if idx != i:
        rst += 1
        continue
    idx += 1
if rst == n:
    print(-1)
else:
    print(rst)