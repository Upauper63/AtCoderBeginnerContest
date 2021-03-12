
import sys
f = open('04_D - Hachi.txt', 'r')
sys.stdin = f

import collections
S = input()
if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()
cnt_ls = collections.Counter(S)
for i in range(100, 1000):
    if i % 8 != 0:
        continue
    tmp = str(i)
    if '0' in tmp:
        continue
    tmp_cnt = cnt_ls.copy()
    rst = True
    for val in tmp:
        if val in tmp_cnt:
            tmp_cnt[val] -= 1
            if tmp_cnt[val] < 0:
                rst = False
                break
        else:
            rst = False
            break
    if rst:
        break
if rst:
    print('Yes')
else:
    print('No')