
import sys
f = open('01.txt', 'r')
sys.stdin = f

N, W = map(int, input().split(' '))
print(N // W)