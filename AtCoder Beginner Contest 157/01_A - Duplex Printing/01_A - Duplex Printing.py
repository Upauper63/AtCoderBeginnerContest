import sys
import os
f = open('01_A - Duplex Printing.txt', 'r')
sys.stdin = f

N = int(input())
print((N + 1) // 2)