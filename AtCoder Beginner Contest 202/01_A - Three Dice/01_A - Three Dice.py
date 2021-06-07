import sys
f = open('01_A - Three Dice.txt', 'r')
sys.stdin = f

a, b, c = map(int, input().split(' '))
print(21 - a - b - c)