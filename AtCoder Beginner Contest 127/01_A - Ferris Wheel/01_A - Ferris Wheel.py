import sys
import os
f = open('01_A - Ferris Wheel.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
if A <= 5:
    print(0)
elif A >= 13:
    print(B)
else:
    print(B // 2)