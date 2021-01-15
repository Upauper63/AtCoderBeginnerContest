import sys
import os
f = open('01_A - Poor.txt', 'r')
sys.stdin = f

ls = list(input().split(' '))
if ls.count(ls[0]) == 2 or ls.count(ls[1]) == 2:
    print('Yes')
else:
    print('No')