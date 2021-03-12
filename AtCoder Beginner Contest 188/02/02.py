
import sys
f = open('02.txt', 'r')
sys.stdin = f

N = int(input())
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
rst = 0
for a, b in zip(a_ls, b_ls):
    rst += a * b
if rst == 0:
    print('Yes')
else:
    print('No')
    