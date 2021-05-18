import sys
f = open('01.txt', 'r')
sys.stdin = f

m, h = map(int, input().split(' '))
if h % m == 0:
    print('Yes')
else:
    print('No')