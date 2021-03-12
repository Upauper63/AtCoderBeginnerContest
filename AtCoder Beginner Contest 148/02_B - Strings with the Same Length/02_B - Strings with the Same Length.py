import sys

f = open('02_B - Strings with the Same Length.txt', 'r')
sys.stdin = f

N = int(input())
S, T = map(list, input().split(' '))
result = ''
for s, t in zip(S, T):
    result = result + s + t
print(result)