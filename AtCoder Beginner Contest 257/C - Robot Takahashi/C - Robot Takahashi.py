import sys
f = open('C - Robot Takahashi.txt', 'r')
sys.stdin = f

n = int(input())
tf = list(map(int, input()))
ls = list(map(int, input().split(' ')))
data = []
wrong_cnt = 0
for t, v in zip(tf, ls):
    if not t:
        wrong_cnt += 1
    data.append([t, v])
if wrong_cnt == 0 or wrong_cnt == n:
    print(n)
    exit()
data = sorted(data, key=lambda x: x[1])
res = n - wrong_cnt
for i in range(n):
    if data[i][0]:
        wrong_cnt += 1
    else:
        wrong_cnt -= 1
    if i == n - 1 or data[i][1] != data[i + 1][1]:
            res = max(res, n - wrong_cnt)
print(res)