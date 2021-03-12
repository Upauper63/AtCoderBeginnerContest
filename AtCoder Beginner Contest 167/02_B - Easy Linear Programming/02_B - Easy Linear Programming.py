import sys

f = open('02_B - Easy Linear Programming.txt', 'r')
sys.stdin = f

A, B, C, K = map(int, input().split())
if A > K:
    print(K)
elif A <= K <= A + B:
    print(A)
else:
    print(A - (K - A - B))