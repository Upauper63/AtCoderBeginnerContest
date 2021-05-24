import sys
f = open('02_B - Intersection.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
val = min(b_ls) - max(a_ls) + 1
if val <= 0:
    print(0)
else:
    print(val)