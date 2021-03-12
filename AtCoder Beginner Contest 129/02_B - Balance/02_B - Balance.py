import sys

f = open('02_B - Balance.txt', 'r')
sys.stdin = f

N = int(input())
W_ls = list(map(int, input().split(' ')))
diff_min = sum(W_ls)
for i in range(len(W_ls)):
    diff_min = min(diff_min, abs(sum(W_ls[:i]) - sum(W_ls[i:])))
print(diff_min)