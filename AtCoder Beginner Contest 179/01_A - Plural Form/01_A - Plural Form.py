import os
import sys
f = open('01_A - Plural Form.txt', 'r')
sys.stdin = f

S = input()
if S[-1:] == 's':
    S += 'es'
    print(S)
else:
    S += 's'
    print(S)