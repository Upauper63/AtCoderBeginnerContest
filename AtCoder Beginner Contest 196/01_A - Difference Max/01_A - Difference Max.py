import sys
f = open('01_A - Difference Max.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))
print(b - c)