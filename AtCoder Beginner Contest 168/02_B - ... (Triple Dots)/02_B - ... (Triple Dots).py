import sys
import os
f = open('02_B - ... (Triple Dots).txt', 'r')
sys.stdin = f

K = int(input())
S = input()
if len(S) > K:
    print('{}...'.format(S[:K]))
else:
    print(S)