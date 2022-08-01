import sys
f = open('B - Number Box.txt', 'r')
sys.stdin = f

n = int(input())
data = []
res = 0
for idx in range(n):
    data.append(list(map(int, input())))
def check(y, x):
    dir_val = ['' for i in range(8)]
    for i in range(n):
        tmp_val = data[(y - i) % n][x]
        dir_val[0] += str(tmp_val)
        tmp_val = data[(y - i) % n][(x + i) % n]
        dir_val[1] += str(tmp_val)
        tmp_val = data[y][(x + i) % n]
        dir_val[2] += str(tmp_val)
        tmp_val = data[(y + i) % n][(x + i) % n]
        dir_val[3] += str(tmp_val)
        tmp_val = data[(y + i) % n][x]
        dir_val[4] += str(tmp_val)
        tmp_val = data[(y + i) % n][(x - i) % n]
        dir_val[5] += str(tmp_val)
        tmp_val = data[y][(x - i) % n]
        dir_val[6] += str(tmp_val)
        tmp_val = data[(y - i) % n][(x - i) % n]
        dir_val[7] += str(tmp_val)    
    val = 0
    for i in range(8):
        val = max(int(dir_val[i]), val)
    return val
for s in range(n):
    for t in range(n):
        res = max(check(s, t), res)
print(res)