import sys
import os
f = open('01_A - A C.txt', 'r')
sys.stdin = f

s = 'ARC' if 'ABC' == input() else 'ABC'
print(s)
