import os
import sys
f = open('01.txt', 'r')
sys.stdin = f

x = int(input())
if x < 0:
    print(0)
else:
    print(x)