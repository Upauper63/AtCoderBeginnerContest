import sys

f = open('03_C - Poll.txt', 'r')
sys.stdin = f

N = int(input())
dic, rst = {}, []
for i in range(N):
    S = input()
    if S in dic:
        dic[S] += 1
    else:
        dic[S] = 1
max_val = max(dic.values())
[ rst.append(key) for key, val in dic.items() if val == max_val ]
[ print(i) for i in sorted(rst) ]