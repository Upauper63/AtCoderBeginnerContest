import sys
import os
f = open('01_A - Harmony.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
if (A + B) % 2 == 0:
    print(int((A + B) / 2))
else:
    print('IMPOSSIBLE')