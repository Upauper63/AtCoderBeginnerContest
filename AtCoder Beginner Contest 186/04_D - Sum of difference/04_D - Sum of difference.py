import sys
f = open('04_D - Sum of difference.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
a_ls.sort(reverse=True)
rst = 0
for k, v in enumerate(a_ls):
    rst += v * (n - k - 1) 
    rst -= v * k
print(rst)