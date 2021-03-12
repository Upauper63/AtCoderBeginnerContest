import sys

f = open('01_A - Red or Not.txt', 'r')
sys.stdin = f

a = int(input())
s = input()
if a < 3200:
    print('red')
else:
    print(s)