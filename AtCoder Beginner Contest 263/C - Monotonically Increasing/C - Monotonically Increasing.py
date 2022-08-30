import sys
f = open('C - Monotonically Increasing.txt', 'r')
sys.stdin = f

n, m = map(int, input().split(' '))
def check(val, t, cnt):
    if cnt == n:
        rst = ''
        for v in val:
            rst += str(v) + ' '
        print(rst)
        return
    else:
        for s in range(t + 1, m + 1):
            tmp = val.copy()
            tmp.append(s)
            check(tmp, s, cnt + 1)
for i in range(1, m - n + 2):
    check([i], i, 1)