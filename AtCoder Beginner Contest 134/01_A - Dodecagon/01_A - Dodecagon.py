import sys
import os
f = open('01_A - Dodecagon.txt', 'r')
sys.stdin = f

r = int(input())
print(3 * r ** 2)