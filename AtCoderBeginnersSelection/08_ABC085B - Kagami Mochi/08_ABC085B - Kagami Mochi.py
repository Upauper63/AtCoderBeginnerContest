import sys
import os
f = open('08_ABC085B - Kagami Mochi.txt', 'r')
sys.stdin = f

n = int(input())
cnt = 0
s = set()
while cnt < n:
    s.add(int(input()))
    cnt += 1
print(len(s))