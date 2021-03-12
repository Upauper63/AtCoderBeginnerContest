
import sys
f = open('01.txt', 'r')
sys.stdin = f

N, A, B = map(int, input().split(' '))
print(N - A + B)