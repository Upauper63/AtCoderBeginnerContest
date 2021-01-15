import os
import sys
f = open('01_A - Air Conditioner.txt', 'r')
sys.stdin = f

X = int(input())
if X >= 30:
    print('Yes')
else:
    print('No')