
import sys
f = open('04_D - Takahashi Unevolved.txt', 'r')
sys.stdin = f

X, Y, A, B = map(int, input().split(' '))
rst = 0
while X < B / (A - 1) and X * A < Y:
    X *= A
    rst += 1
print((Y - X - 1) // B + rst)