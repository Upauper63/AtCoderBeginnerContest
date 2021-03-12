
import sys
f = open('01_A - Rainy Season.txt', 'r')
sys.stdin = f

S = input()
cnt, rst = 0, 0
for i in S:
    if i == 'R':
        cnt += 1
    else:
        cnt = 0
    rst = max(rst, cnt)
print(rst)