import sys
f = open('C - Filling 3x3 array.txt', 'r')
sys.stdin = f

ls = list(map(int, input().split(' ')))
h_ls = ls[:3]
w_ls = ls[3:]
res = 0
for a in range(1, 31):
    for b in range(1, 31):
        c = h_ls[0] - a - b
        if c > 0:
            for d in range(1, 31):
                for e in range(1, 31):
                    f = h_ls[1] - d - e
                    g = w_ls[0] - a - d
                    h = w_ls[1] - b - e
                    i = h_ls[2] - g - h
                    if f > 0 and g > 0 and h > 0 and i > 0 and i == w_ls[2] - c - f:
                        res += 1
                    if f <= 0:
                        break
        else:
            break
print(res)