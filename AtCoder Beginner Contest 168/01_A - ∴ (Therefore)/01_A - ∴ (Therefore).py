import sys
import os
f = open('01_A - ∴ (Therefore).txt', 'r')
sys.stdin = f

s = input()
s = int(s[-1])
if s in [2,4,5,7,9]:
    print('hon')
elif s in [0,1,6,8]:
    print('pon')
else:
    print('bon')