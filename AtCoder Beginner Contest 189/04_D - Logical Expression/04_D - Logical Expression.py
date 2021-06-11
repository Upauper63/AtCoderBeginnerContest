import sys
f = open('04_D - Logical Expression.txt', 'r')
sys.stdin = f

n = int(input())
y = [[] for i in range(n + 1)]
y[0] = 1
for i in range(1, n + 1):
    s = input()
    if s == 'OR':
        y[i] = 2 ** (i) + y[i - 1]
    else:
        y[i] = y[i - 1]
print(y[n])