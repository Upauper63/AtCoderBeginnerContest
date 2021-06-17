import sys
f = open('04_D - Powerful Discount Tickets.txt', 'r')
sys.stdin = f

import heapq
n, m = map(int, input().split(' '))
a_ls = list(map(lambda x: int(x) * -1, input().split(' ')))
heapq.heapify(a_ls)
for _ in range(m):
    val = - 1 * heapq.heappop(a_ls) // 2
    heapq.heappush(a_ls, -1 * val)
print(sum(a_ls) * -1)