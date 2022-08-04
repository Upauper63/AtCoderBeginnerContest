import sys
f = open('B - 1D Pawn.txt', 'r')
sys.stdin = f

n, k, q = map(int, input().split(' '))
a_ls = map(int, input().split(' '))
k_ls = map(int, input().split(' '))
dic = {}
ls = [False for i in range(n)]
for i, v in enumerate(a_ls):
    dic[i + 1] = v
    ls[v - 1] = True
for i in k_ls:
    v = dic[i]
    if v >= n or ls[v]:
        continue
    else:
        ls[v] = True
        ls[v - 1] = False
        dic[i] = v + 1
[print(v, end=" ") for v in dic.values()]