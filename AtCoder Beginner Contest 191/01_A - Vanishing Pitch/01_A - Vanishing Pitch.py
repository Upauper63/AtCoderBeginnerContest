
import sys
f = open('01_A - Vanishing Pitch.txt', 'r')
sys.stdin = f

V, T, S, D = map(int, input().split(' '))
if D < V * T or V * S < D:
    print('Yes')
else:
    print('No')