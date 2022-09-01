import sys
f = open('B - Explore.txt', 'r')
sys.stdin = f

n, m, t = map(int, input().split(' '))
def int_minus(x):
    return - 1 * int(x)
a_ls = list(map(int_minus, input().split(' ')))
a_cumsum = [0 for i in range(n)]
a_cumsum[0] = t
for i in range(m):
    x, y = map(int, input().split(' '))
    a_cumsum[x] += y
for i in range(n - 1):
    a_cumsum[i + 1] += a_cumsum[i] + a_ls[i]
    if a_cumsum[i + 1] <= 0:
        print('No')
        exit()
print('Yes')