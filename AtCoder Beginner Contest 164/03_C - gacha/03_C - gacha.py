import sys

f = open('03_C - gacha.txt', 'r')
sys.stdin = f

N = int(input())
S = { input() for i in range(N) }
print(len(S))