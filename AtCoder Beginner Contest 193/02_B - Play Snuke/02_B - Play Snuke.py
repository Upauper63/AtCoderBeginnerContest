
import sys
f = open('02_B - Play Snuke.txt', 'r')
sys.stdin = f

N = int(input())
ls = [list(map(int, input().split(' '))) for _ in range(N)]
ls = sorted(ls, key=lambda x: x[1])
for a, p, x in ls:
    if int(x - a) > 0:
        print(p)
        exit()
print(-1)