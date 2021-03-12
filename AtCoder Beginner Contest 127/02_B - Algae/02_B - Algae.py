import sys

f = open('02_B - Algae.txt', 'r')
sys.stdin = f

r, D, x = map(int, input().split(' '))
for i in range(10):
    x = r * x - D
    print(x)