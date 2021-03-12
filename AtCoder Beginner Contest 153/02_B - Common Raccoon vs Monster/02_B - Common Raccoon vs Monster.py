import sys

f = open('02_B - Common Raccoon vs Monster.txt', 'r')
sys.stdin = f

H, N = map(int, input().split(' '))
A_ls = map(int, input().split(' '))
if sum(A_ls) >= H:
    print('Yes')
else:
    print('No')