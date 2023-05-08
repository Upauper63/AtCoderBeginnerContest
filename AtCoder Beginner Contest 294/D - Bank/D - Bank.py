import sys
f = open('D - Bank.txt', 'r')
sys.stdin = f

from collections import defaultdict
n, q = map(int, input().split(' '))
idx = 0
called_ls = defaultdict(lambda: False)
for i in range(q):
    e_ls = list(map(int, input().split(' ')))
    if e_ls[0] == 2:
        called_ls[e_ls[1] - 1] = True
    elif e_ls[0] == 3:
        while called_ls[idx]:
            idx += 1
        print(idx + 1)

# n, q = map(int, input().split(' '))
# cnt = 1
# called_ls = set()
# for i in range(q):
#     e_ls = list(map(int, input().split(' ')))
#     if e_ls[0] == 1:
#         called_ls.add(cnt)
#         cnt += 1
#     elif e_ls[0] == 2:        
#         called_ls.remove(e_ls[1])
#     else:
#         print(min(called_ls))