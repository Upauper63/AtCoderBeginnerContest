import sys
f = open('B - Batters.txt', 'r')
sys.stdin = f

n = int(input())
ls = list(map(int, input().split(' ')))
data = [0]
res = 0
def addNum(v, num):
    return v + num
for s in ls:
    tmp = []
    for t in data:
        if (t + s) // 4:
            res += 1
        else:
            tmp.append(t + s)
    data = tmp
    data.append(0)
print(res)