
import sys
f = open('04_D - Lunlun Number.txt', 'r')
sys.stdin = f

K = int(input())

import sys
f = open('04_D - Lunlun Number.txt', 'r')
sys.stdin = f

K = int(input())
lunlun = [i for i in range(1, 10)]
p = 0
while len(lunlun) < K:
    last = lunlun[p] % 10
    if last - 1 >= 0:
        lunlun.append(lunlun[p] * 10 + last - 1)
    lunlun.append(lunlun[p] * 10 + last)
    if last + 1 <= 9:
        lunlun.append(lunlun[p] * 10 + last + 1)
    p += 1
print(lunlun[K - 1])