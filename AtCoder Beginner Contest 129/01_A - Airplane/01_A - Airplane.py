import sys
import os
f = open('01_A - Airplane.txt', 'r')
sys.stdin = f

P, Q, R = map(int, input().split(' '))
print(min([P+Q, Q+R, R+P]))