import sys
f = open('A - 2^N.txt', 'r')
sys.stdin = f

n = int(input())
ans = 1
if n:
    for i in range(n):
        ans *= 2
print(ans)