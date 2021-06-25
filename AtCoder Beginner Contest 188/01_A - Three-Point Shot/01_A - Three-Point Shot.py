
import sys
f = open('01.txt', 'r')
sys.stdin = f

X, Y = map(int, input().split(' '))
low = min([X, Y])
high = max([X, Y])
if low + 3 > high:
    print('Yes')
else:
    print('No')