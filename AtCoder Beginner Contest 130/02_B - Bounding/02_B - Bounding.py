import sys

f = open('02_B - Bounding.txt', 'r')
sys.stdin = f

N, X = map(int, input().split(' '))
L_ls = map(int, input().split(' '))
D, cnt = 0, 1
for L in L_ls:
    D += L
    if D > X:
        break
    cnt += 1
print(cnt)