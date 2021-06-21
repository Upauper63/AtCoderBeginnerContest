
import sys
f = open('03_C - Kaprekar Number.txt', 'r')
sys.stdin = f

N, K = input().split(' ')
N = list(N)
K = int(K)
for i in range(K):
    g1 = ''.join((sorted(N)))
    g2 = ''.join((sorted(N, reverse=True)))
    N = int(g2) - int(g1)
    N = list(str(N))
print(''.join(N))