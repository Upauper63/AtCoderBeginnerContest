
import sys
f = open('04_D - Redistribution.txt', 'r')
sys.stdin = f

S = int(input())
dp = [0 for i in range(S + 1)]
dp[0] = 1
for i in range(1, S + 1):
    for j in range(0, i - 3 + 1):
        dp[i] += dp[j]
print(dp[S] % (10 ** 9 + 7))