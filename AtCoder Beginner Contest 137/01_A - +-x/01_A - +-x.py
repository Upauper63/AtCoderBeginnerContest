import sys
import os
f = open('01_A - +-x.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
print(max([A + B, A - B, A * B]))