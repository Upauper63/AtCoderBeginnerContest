import sys
f = open('01_A - Your First Judge.txt', 'r')
sys.stdin = f

s = input()
if s == 'Hello,World!':
    print('AC')
else:
    print('WA')