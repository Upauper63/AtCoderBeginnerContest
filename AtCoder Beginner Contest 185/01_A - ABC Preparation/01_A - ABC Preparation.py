
import sys
f = open('01.txt', 'r')
sys.stdin = f

ls = list(map(int, input().split(' ')))
print(min(ls))