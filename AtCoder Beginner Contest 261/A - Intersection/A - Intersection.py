import sys
f = open('A - Intersection.txt', 'r')
sys.stdin = f

l1, r1, l2, r2 = map(int, input().split(' '))
minr = min(r1, r2)
maxl = max(l1, l2)
res = minr - maxl
if res > 0:
    print(res)
else:
    print(0)
