import sys
f = open('01_A - Bitwise Exclusive Or.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
print(a ^ b)