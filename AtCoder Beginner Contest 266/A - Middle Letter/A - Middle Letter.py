import sys
f = open('A - Middle Letter.txt', 'r')
sys.stdin = f

s = input()
print(s[len(s) // 2])