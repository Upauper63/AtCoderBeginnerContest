import sys

f = open('01_A - 500 Yen Coins.txt', 'r')
sys.stdin = f

K, X = map(int, input().split(' '))
if 500 * K >= X:
    print('Yes')
else:
    print('No')