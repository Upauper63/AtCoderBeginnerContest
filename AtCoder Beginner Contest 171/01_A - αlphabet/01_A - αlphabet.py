import sys
import os
f = open('01_A - αlphabet.txt', 'r')
sys.stdin = f

s = input()
if s <= 'Z':
    print('A')
else:
    print('a')