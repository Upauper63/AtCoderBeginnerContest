import sys

f = open('02_B - Ordinary Number.txt', 'r')
sys.stdin = f

n = int(input())
p_ls = list(map(int, input().split(' ')))
cnt = 0
for i in range(1, len(p_ls) - 1):
    if (p_ls[i-1] < p_ls[i] < p_ls[i+1]) or (p_ls[i+1] < p_ls[i] < p_ls[i-1]):
        cnt += 1
print(cnt)