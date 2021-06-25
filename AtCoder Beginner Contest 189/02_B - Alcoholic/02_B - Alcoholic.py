
import sys
f = open('02.txt', 'r')
sys.stdin = f

N, X = map(int, input().split(' '))
X *= 100
cnt, rst = 0, 0
for i in range(N):
    V, P = map(int, input().split(' '))
    rst += V * P
    cnt += 1
    if rst > X:
        print(cnt)
        exit()
print(-1)