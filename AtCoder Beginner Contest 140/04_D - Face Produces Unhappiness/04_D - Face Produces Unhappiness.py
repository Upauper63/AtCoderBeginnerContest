import sys
f = open('04_D - Face Produces Unhappiness.txt', 'r')
sys.stdin = f

n, k = map(int, input().split(' '))
s = input()
cnt = 0
for i, j in enumerate(s[1:]):
    if j != s[i]:
        cnt += 1
print(n - 1 - max(0, cnt - 2 * k))