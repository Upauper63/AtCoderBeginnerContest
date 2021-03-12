
import sys
f = open('02_B - Go to Jail.txt', 'r')
sys.stdin = f

N = int(input())
cnt, rst = 0, 0
for i in range(N):
    d1, d2 = map(int, input().split(' '))
    if d1 == d2:
        cnt += 1
    else:
        rst = max(rst, cnt)
        cnt = 0
if rst >= 3 or cnt >= 3:
    print('Yes')
else:
    print('No')