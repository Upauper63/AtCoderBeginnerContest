import sys
f = open('04_D - ModSum.txt', 'r')
sys.stdin = f

n = int(input())
print((n - 1) * n // 2)