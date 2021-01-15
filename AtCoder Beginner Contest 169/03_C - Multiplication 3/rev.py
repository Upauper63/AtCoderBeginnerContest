import os
import sys
f = open('03_C - Multiplication 3.txt', 'r')
sys.stdin = f

A, B = input().split(' ')
print(int(A) * int(B.replace('.', '')) // 100)