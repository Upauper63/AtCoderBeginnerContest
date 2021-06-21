import sys
f = open('02_B - Job Assignment.txt', 'r')
sys.stdin = f


N = int(input())
cnt_ls = [list(map(int, input().split(' '))) for _ in range(N)]
tmp_val = float('inf')
for i in range(N):
    for j in range(N):
        if i == j:
            if cnt_ls[i][0] + cnt_ls[j][1] < tmp_val:
                tmp_val = cnt_ls[i][0] + cnt_ls[j][1]
        else:
            if max(cnt_ls[i][0], cnt_ls[j][1]) < tmp_val:
                tmp_val = max(cnt_ls[i][0], cnt_ls[j][1])
print(tmp_val)