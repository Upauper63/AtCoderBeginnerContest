import sys
import os
f = open('01_A - ABC Swap.txt', 'r')
sys.stdin = f

a, b, c = input().split(' ')
print("{} {} {}".format(c, a, b))