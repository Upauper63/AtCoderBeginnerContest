import sys
f = open('04_D - Rain Flows into Dams.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
rst = []
x1 = sum(a_ls[0::2]) - sum(a_ls[1::2])
rst.append(x1)
for k, v in enumerate(a_ls[:-1]):
    rst.append((v - rst[k] // 2) * 2)
for i in rst:
    print(i)