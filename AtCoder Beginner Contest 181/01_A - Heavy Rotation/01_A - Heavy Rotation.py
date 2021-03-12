
import sys
f = open('01.txt', 'r')
sys.stdin = f

N = int(input())
if N % 2 == 0:
    print('White')
else:
    print('Black')