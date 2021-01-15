import os
import sys
f = open('01.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))
print(a * d - c * b)