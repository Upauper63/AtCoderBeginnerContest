import sys
f = open('01_A - Blood Pressure.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
print((a + 2 * b) / 3)