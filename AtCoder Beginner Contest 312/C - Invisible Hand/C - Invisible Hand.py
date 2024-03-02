import sys
f = open('C - Invisible Hand.txt', 'r')
sys.stdin = f

m, n = map(int, input().split(' '))
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
a_ls.sort()
b_ls.sort(reverse=True)
for k, v in enumerate(a_ls):
    if k + 2 > n:
        print(v)
        exit()
    if b_ls[k + 1] >= v:
        continue
    if b_ls[k + 1] < v < b_ls[k]:
        print(v)
        exit()
    else:
        print(b_ls[0] + 1)
        exit()
print(b_ls[0] + 1)