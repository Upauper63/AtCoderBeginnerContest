import sys
f = open('01_A - Counting.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
if a > b:
    print(0)
else:
    print(b - a + 1)