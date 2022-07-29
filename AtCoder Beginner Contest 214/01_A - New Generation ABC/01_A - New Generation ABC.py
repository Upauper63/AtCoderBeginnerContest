import sys
f = open('01_A - New Generation ABC.txt', 'r')
sys.stdin = f

n = int(input())
if n > 211:
    print(8)
elif n > 125:
    print(6)
else:
    print(4)