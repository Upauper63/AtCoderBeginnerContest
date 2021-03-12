
import sys
f = open('04_D - increment of coins.txt', 'r')
sys.stdin = f

A, B, C = map(int, input().split(' '))
dp = [ [ [0] * 101 for i in range(101) ] for j in range(101) ]
dp[A][B][C] = 1
rst = 0
for i in range(A, 101):
    for j in range(B, 101):
        for k in range(C, 101):
            if i == 100 or j == 100 or k == 100:
                rst += dp[i][j][k] * ((i + j + k) - (A + B + C))
                continue
            dp[i + 1][j][k] += (i / (i + j + k)) * dp[i][j][k]
            dp[i][j + 1][k] += (j / (i + j + k)) * dp[i][j][k]
            dp[i][j][k + 1] += (k / (i + j + k)) * dp[i][j][k]
print(rst)