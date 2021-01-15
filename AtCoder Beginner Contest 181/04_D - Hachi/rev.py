import os
import sys
f = open('04_D - Hachi.txt', 'r')
sys.stdin = f

S = input()
if len(S) < 3:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()