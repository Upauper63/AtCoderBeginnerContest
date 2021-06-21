
import sys
f = open('01_A - Brick.txt', 'r')
sys.stdin = f

N, W = map(int, input().split(' '))
print(N // W)