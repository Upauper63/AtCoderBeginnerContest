import sys
import os
f = open('01_.txt', 'r')
sys.stdin = f

n = int(input())
print(abs((1000 - n) % 1000))