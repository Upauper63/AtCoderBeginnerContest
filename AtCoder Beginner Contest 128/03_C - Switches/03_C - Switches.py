
import sys
f = open('03_C - Switches.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
S_ls = []
rst = 0
for i in range(M):
    ls = list(map(int, input().split(' ')))
    S_ls.append(ls[1:])

M_ls = list(map(int, input().split(' ')))

for i in range(1 << N):
    ls = [ 0 for i in range(N) ]
    for j in range(N):
        if i >> j & 1:
            ls[j] = 1

    is_OK = True
    for idx, s in enumerate(S_ls):
        cnt = 0
        for t in s:
            if ls[t - 1]:
                cnt += 1
        if M_ls[idx] != cnt % 2:
            is_OK = False
            break
    
    if is_OK:
        rst += 1

print(rst)