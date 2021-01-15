import sys
import os
f = open('02_B - Judge Status Summary.txt', 'r')
sys.stdin = f

N = int(input())
dict = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for i in range(N):
    S = input()
    dict[S] += 1
for key, value in dict.items():
    print('{} x {}'.format(key, value))