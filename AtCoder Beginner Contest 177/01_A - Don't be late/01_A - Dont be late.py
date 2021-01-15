import os
import sys
f = open('01_A - Dont be late.txt', 'r')
sys.stdin = f

D, T, S = map(int, input().split(' '))
if T * S >= D:
    print('Yes')
else:
    print('No')