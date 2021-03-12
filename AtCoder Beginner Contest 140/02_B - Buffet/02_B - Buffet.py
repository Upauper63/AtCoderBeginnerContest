import sys

f = open('02_B - Buffet.txt', 'r')
sys.stdin = f

N = int(input())
A_ls = map(int, input().split(' '))
B_ls = list(map(int, input().split(' ')))
C_ls = list(map(int, input().split(' ')))

result = 0
tmp = 0
for A in A_ls:
    if (A - tmp) == 1 and tmp != 0:
        result += B_ls[A-1] + C_ls[A-2]
    else:
        result += B_ls[A-1]
    tmp = A
print(result)