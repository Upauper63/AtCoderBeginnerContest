import sys
f = open('04_D - equeue.txt', 'r')
sys.stdin = f

import collections
import heapq
v, k = map(int, input().split(' '))
dq = collections.deque(map(int, input().split(' ')))

def pick_fr_left(j, ls):
    cnt = 0
    while len(tmp_dq) > 0 and cnt < j:
        heapq.heappush(ls, tmp_dq.popleft())
        cnt += 1
    return ls
def pick_fr_right(i, j, ls):
    cnt = 0
    while len(tmp_dq) > 0 and cnt < i - j:
        heapq.heappush(ls, tmp_dq.pop())
        cnt += 1
    return ls

def get_back(i, ls):
    cnt = 0
    while len(ls) > 0 and ls[0] < 0 and cnt < k - i:
        heapq.heappop(ls)
        cnt += 1
    return ls

rst = 0
for i in range(k + 1):
    for j in range(i + 1):
        tmp_dq = dq.copy()
        ls = []
        ls = pick_fr_left(j, ls)
        ls = pick_fr_right(i, j, ls)
        ls = get_back(i, ls)
        val = 0
        while ls:
            val += ls.pop()
        rst = max(val, rst)
print(rst)