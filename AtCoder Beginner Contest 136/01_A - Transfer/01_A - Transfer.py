import sys

f = open('01_A - Transfer.txt', 'r')
sys.stdin = f

A, B, C = map(int, input().split(' '))
if A - B > C:
    print(0)
else:
    print(C - (A - B))
