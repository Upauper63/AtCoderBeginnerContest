import sys
import os
f = open('02_ABC086A - Product.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
if (a * b) % 2 == 0:
    print('Even')
else:
    print('Odd')