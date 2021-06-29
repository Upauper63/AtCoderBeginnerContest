import sys
f = open('04_D - Preparing Boxes.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
ls = [0] * n
for i in range(n - 1, -1, -1):
    tmp_val = a_ls[i]
    if sum(ls[i::i+1]) % 2 != tmp_val:
        ls[i] += 1 
    sum_val = a_ls[i::i+1]
m = sum(ls)
if m == 0:
    print(0)
else:
    print(m)
    for k, v in enumerate(ls):
        if v == 1:
            print(k + 1)