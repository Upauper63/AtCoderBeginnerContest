import sys
f = open('04_D - Enough Array.txt', 'r')
sys.stdin = f

n, k = map(int, input().split(' '))
a_ls = list(map(int, input().split(' ')))
rst = 0
val = 0
left = 0
for right in range(n):
    val += a_ls[right]
    while val >= k:
        rst += n - right
        val -= a_ls[left]
        left += 1
print(rst)