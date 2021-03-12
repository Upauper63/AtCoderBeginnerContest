import sys

f = open('03_C - Guess The Number.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
rst_ls = [ '' for i in range(N) ]
rst = ''
if M == 0:
    if N == 1:
        print(0)
    else:
        rst = '1' + '0' * (N - 1)
        print(rst)
else:
    is_end = False
    for i in range(M):
        ls = list(input().split(' '))
        idx = int(ls[0]) - 1
        if idx == 0 and ls[1] == '0' and N > 1:
            is_end = True
            print(-1)
            break
        elif rst_ls[idx] == '':
            rst_ls[idx] = ls[1]
        elif rst_ls[idx] != ls[1]:
            is_end = True
            print(-1)
            break
    if not is_end:
        if rst_ls[0] == '' and N > 1:
            rst_ls[0] = 1
        for i in rst_ls:
            if i == '':
                i = 0
            print(i, end='')