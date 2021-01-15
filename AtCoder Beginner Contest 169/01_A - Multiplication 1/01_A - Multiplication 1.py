import sys
import os
f = open('01_A - Multiplication 1.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
print(a * b)