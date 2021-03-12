import sys

f = open('01_A - Five Variables.txt', 'r')
sys.stdin = f

s = input().split(' ')
print(s.index('0') + 1)