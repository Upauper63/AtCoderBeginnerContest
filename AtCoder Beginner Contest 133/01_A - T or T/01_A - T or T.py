import sys
import os
f = open('01_A - T or T.txt', 'r')
sys.stdin = f

N, A, B = map(int, input().split(' '))
print(min(N * A, B))