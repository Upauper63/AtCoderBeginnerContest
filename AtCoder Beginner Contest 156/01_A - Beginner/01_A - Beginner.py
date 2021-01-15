import sys
import os
f = open('01_A - Beginner.txt', 'r')
sys.stdin = f

N, R = map(int, input().split(' '))
if N >= 10:
    print(R)
else:
    print(R + 100 * (10 - N))