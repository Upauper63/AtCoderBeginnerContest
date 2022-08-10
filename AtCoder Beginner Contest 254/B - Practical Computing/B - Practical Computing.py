import sys
f = open('B - Practical Computing.txt', 'r')
sys.stdin = f

n = int(input())
res = [1]
for i in range(n):
    tmp = []
    if i != 0:
        print('1', end=" ")
    tmp.append(1)
    for j in range(1, i):
        print(res[j - 1] + res[j], end=" ")
        tmp.append(res[j - 1] + res[j])
    print('1')
    tmp.append(1)
    res = tmp