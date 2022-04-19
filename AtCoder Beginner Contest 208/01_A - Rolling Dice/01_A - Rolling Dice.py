import sys
f = open('01_A - Rolling Dice.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
if a <= b <= 6 * a:
    print('Yes')
else:
    print('No')