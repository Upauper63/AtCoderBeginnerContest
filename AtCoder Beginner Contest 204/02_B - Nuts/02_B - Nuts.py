import sys
f = open('02_B - Nuts.txt', 'r')
sys.stdin = f

n = int(input())
def int_minus10(x):
    return int(x) - 10
a_ls = list(map(int_minus10, input().split(' ')))
rst = 0
for a in a_ls:
    if a >= 0:
        rst += a
print(rst)