import sys
import os
f = open('01_A - Registration.txt', 'r')
sys.stdin = f

s = input()
t = input()[0:-1]
if s == t:
    print('Yes')
else:
    print('No')
