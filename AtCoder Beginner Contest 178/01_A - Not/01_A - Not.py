import os
import sys
f = open('01_A - Not.txt', 'r')
sys.stdin = f

var = 1 if input() == '0' else 0
print(var)