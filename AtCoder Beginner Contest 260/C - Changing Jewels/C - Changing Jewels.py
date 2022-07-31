import sys
f = open('C - Changing Jewels.txt', 'r')
sys.stdin = f

n, x, y = map(int, input().split(' '))
# lv, r num, b num
data = [n, 1, 0]
res = 0
def devide_rec(data):
    if data[0] == 1:
        return data
    else:
        data[0] -= 1
        tmp = data[2] + data[1] * x
        data[1] += tmp
        data[2] = tmp * y
        return devide_rec(data)
res = devide_rec(data)
print(res[2])