
import sys
f = open('03.txt', 'r')
sys.stdin = f

H, W = map(int, input().split(' '))
ls = [[] for i in range(H)]
for i in range(H):
    ls[i] = list(input())
rst = 0
for i in range(H - 1):
    for j in range(W - 1):
        bl_cnt, wh_cnt = 0, 0
        if ls[i][j] == '#':
            bl_cnt += 1
        else:
            wh_cnt += 1
        if ls[i][j + 1] == '#':
            bl_cnt += 1
        else:
            wh_cnt += 1
        if ls[i + 1][j] == '#':
            bl_cnt += 1
        else:
            wh_cnt += 1
        if ls[i + 1][j + 1] == '#':
            bl_cnt += 1
        else:
            wh_cnt += 1
        if wh_cnt == 3 or bl_cnt == 3:
            rst += 1
print(rst)
        