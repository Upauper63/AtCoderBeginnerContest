import sys
f = open('04_D - Cooking.txt', 'r')
sys.stdin = f

n = int(input())
t_ls = list(map(int, input().split(' ')))
sum_t = sum(t_ls)
dp = [False] * (sum_t + 1)
dp[0] = True
for t in t_ls:
    for i in range(sum_t, t - 1, -1):
        if dp[i - t]:
            dp[i] = dp[i - t]
val = (sum_t + 1) // 2
while dp[val] == False:
    val += 1
print(val)