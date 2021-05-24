import sys
f = open('01_A - Square Inequality.txt', 'r')
sys.stdin = f

a, b, c = map(int, input().split(' '))
if a ** 2 + b ** 2 < c ** 2:
    print('Yes')
else:
    print('No')