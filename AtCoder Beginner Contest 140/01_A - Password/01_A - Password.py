import sys
import os
f = open('01_A - Password.txt', 'r')
sys.stdin = f

N = int(input())
print(N ** 3)