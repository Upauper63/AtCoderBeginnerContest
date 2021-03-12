import sys

f = open('02_B - Comparing Strings.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
if a > b:
    print(str(b) * a)
else:
    print(str(a) * b)