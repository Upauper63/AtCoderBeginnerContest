from opcode import opname
import sys
f = open('C - Min Max Pair.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
rst = 0
idx_eq_val_ls = []
for i, v in enumerate(a_ls):
    if i + 1 == v:
        idx_eq_val_ls.append(v)
    else:
        if v - 1 > i and a_ls[v - 1] == i + 1:
            rst += 1
idx_eq_val_ls.sort()
tmp_idx = 0
for s in idx_eq_val_ls:
    for j, t in enumerate(idx_eq_val_ls[tmp_idx:]):
        if s < t:
            if tmp_idx:
                rst += len(idx_eq_val_ls) - (j + tmp_idx)
            else:
                rst += len(idx_eq_val_ls) - j
            tmp_idx = j
            break
print(rst)