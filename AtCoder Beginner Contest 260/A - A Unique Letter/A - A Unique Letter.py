import sys
f = open('A - A Unique Letter.txt', 'r')
sys.stdin = f

s = input()
counter = {}
for v in s:
    if v in counter:
        counter[v] += 1
    else:
        counter[v] = 1
for k, v in counter.items():
    if v == 1:
        print(k)
        exit()
print(-1)