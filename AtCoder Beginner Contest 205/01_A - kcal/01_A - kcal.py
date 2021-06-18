import sys
f = open('01_A - kcal.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
print(a * b / 100)