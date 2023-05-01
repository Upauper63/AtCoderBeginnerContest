import sys
f = open('C - Cross.txt', 'r')
sys.stdin = f

h, w = map(int, input().split(' '))
maze = [list(input()) for _ in range(h)]
n = min(h, w)
cnt = [0 for _ in range(n)]

def check(a, b, d):
    is_ok = True
    if a + d >= h or a - d < 0 or b + d >= w or b - d < 0: is_ok = False
    if is_ok:
        if maze[a + d][b + d] == '.': is_ok = False
        if maze[a + d][b - d] == '.': is_ok = False
        if maze[a - d][b + d] == '.': is_ok = False
        if maze[a - d][b - d] == '.': is_ok = False
    return is_ok

for i in range(h):
    for j in range(w):
        if maze[i][j] == '#':
            is_ok = True
        else:
            is_ok = False
        d = 0
        while is_ok:
            d += 1
            is_ok = check(i, j, d)
        if d > 1:
            cnt[d - 2] += 1
print(' '.join([str(n) for n in cnt]))