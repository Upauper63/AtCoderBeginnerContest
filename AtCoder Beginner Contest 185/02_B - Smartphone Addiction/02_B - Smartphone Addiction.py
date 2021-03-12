
import sys
f = open('02.txt', 'r')
sys.stdin = f

N, M, T = map(int, input().split(' '))
ls = []
tmp = 0
val = N
for i in range(M):
    a, b = map(int, input().split(' '))
    val -= a - tmp
    if val <= 0:
        print('No')
        exit()
    val += b - a
    if val > N:
        val = N
    tmp = b
val -= T - tmp
if val <= 0:
    print('No')
else:
    print('Yes')