import sys
f = open('C - K Swap.txt', 'r')
sys.stdin = f

n, k = map(int, input().split(' '))
res = [[] for i in range(k)]
a_ls = list(map(int, input().split(' ')))
for i in range(k):
    tmp = i
    while tmp < n:
        res[i].append(a_ls[tmp])
        tmp += k
for i in range(k):
    res[i].sort()
tmp = 0
for i in range(n // k):
    for j in range(k):
        if tmp > res[j][i]:
            print('No')
            exit()
        tmp = res[j][i]

for i in range(n % k):
    if tmp > res[i][n // k]:
            print('No')
            exit()
    tmp = res[i][n // k]
print('Yes')