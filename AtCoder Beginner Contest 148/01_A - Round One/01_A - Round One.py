import sys
import os
f = open('01_A - Round One.txt', 'r')
sys.stdin = f

S = '123'
for i in range(2):
    tmp = input()
    S = S.replace(tmp, '')
print(S)