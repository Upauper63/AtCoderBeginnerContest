import sys
f = open('01_A - Century.txt', 'r')
sys.stdin = f

n = int(input())
print((n - 1) // 100 + 1)