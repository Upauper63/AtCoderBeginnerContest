import os
import sys
f = open('01.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
print((2 * A + 100) - B)