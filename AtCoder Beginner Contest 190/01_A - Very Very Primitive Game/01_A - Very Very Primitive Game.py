import sys
f = open('01_A - Very Very Primitive Game.txt', 'r')
sys.stdin = f

a, b, c = map(int, input().split(' '))
if (c == 0 and a <= b) or (c == 1 and a < b):
    print('Aoki')
else:
    print('Takahashi')