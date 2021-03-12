
import sys
f = open('04_D - Sum of Large Numbers.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
rst = 0
for i in range(K, N + 2):
    rst += (N - i + 1) * i + 1
    rst %= 10 ** 9 + 7
print(rst)