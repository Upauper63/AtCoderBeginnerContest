import sys

f = open('02_B - Achieve the Goal.txt', 'r')
sys.stdin = f

N, K, M = map(int, input().split(' '))
A_ls = list(map(int, input().split(' ')))
result = M * N - sum(A_ls)
if result > K:
    print('-1')
elif result < 0:
    print(0)
else:
    print(result)