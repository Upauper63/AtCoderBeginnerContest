import sys
f = open('03_C - IPFL.txt', 'r')
sys.stdin = f

n = int(input())
s = input()
q = int(input())
is_flip = False
idx = [i for i in range(2 * n)]
for i in range(q):
    t, a, b = map(int, input().split(' '))
    if t == 1:
        if is_flip:
            if a < n:
                a += n
            else:
                a -= n
            if b < n:
                b += n
            else:
                b -= n
        val_a = idx[a - 1]
        val_b = idx[b - 1]
        idx[a - 1] = val_b
        idx[b - 1] = val_a
    else:
        is_flip = not is_flip
rst = ''
if is_flip:
    idx = idx[n:] + idx[:n]
for i in idx:
    rst += s[i]
print(rst)