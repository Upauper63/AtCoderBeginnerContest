
import sys
f = open('04_D - Not Divisible.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
max_val = max(ls)
cnt_ls = [0 for i in range(max_val + 1)]
for i in ls:
    val = i
    while val <= max_val:
        cnt_ls[val] += 1
        val += i
rst = 0
for i in ls:
    if cnt_ls[i] == 1:
        rst += 1
print(rst)