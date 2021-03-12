import sys

f = open('01_A - Apple Pie.txt', 'r')
sys.stdin = f

A, P = map(int, input().split(' '))
print((A * 3 + P) // 2)