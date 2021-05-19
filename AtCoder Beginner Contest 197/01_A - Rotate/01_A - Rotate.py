import sys
f = open('01_A - Rotate.txt', 'r')
sys.stdin = f

s = input()
print(s[1:] + s[0])