import sys

f = open('02_B - Multiple of 9.txt', 'r')
sys.stdin = f

N = input()
rst = 0
for i in N:
    rst += int(i)
if rst % 9 == 0:
    print('Yes')
else:
    print('No')