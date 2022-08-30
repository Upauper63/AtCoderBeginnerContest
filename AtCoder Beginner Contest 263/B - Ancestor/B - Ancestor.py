import sys
from tabnanny import check
f = open('B - Ancestor.txt', 'r')
sys.stdin = f

n = int(input())
p_ls = [0, 0] + list(map(int, input().split(' ')))
def check(p, cnt):
    cnt += 1
    if p == 1:
        return cnt
    return check(p_ls[p], cnt)
print(check(p_ls[n], 0))
