import sys
f = open('A - Full House.txt', 'r')
sys.stdin = f

from collections import defaultdict
dic = defaultdict(int)
ls = list(map(int, input().split(' ')))
for v in ls:
    dic[v] += 1
rst = sorted(dic.values())
if len(rst) == 2 and rst[0] == 2 and rst[1] == 3:
    print('Yes')
else:
    print('No')