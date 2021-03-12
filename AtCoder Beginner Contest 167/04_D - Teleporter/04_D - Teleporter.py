
import sys
f = open('04_D - Teleporter.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
cnt_ls = [0 for i in range(N)]
loop_ls = []
cnt, pre = 0, 0
is_loop = False
for i in range(K):
    cnt = ls[cnt] - 1
    cnt_ls[cnt] += 1
    if cnt_ls[cnt] == 2:
        loop_ls.append(cnt)
    if cnt_ls[cnt] == 3:
        is_loop = True
        break
    pre += 1
if is_loop:
    print(loop_ls[(K - pre) % len(loop_ls) - 1] + 1)
else:
    print(cnt + 1)