import sys
f = open('01_A - Cabbages.txt', 'r')
sys.stdin = f

n, a, x, y = map(int, input().split(' '))
if n <= a:
    print(x * n)
else:
    print(x * a + y * (n - a))