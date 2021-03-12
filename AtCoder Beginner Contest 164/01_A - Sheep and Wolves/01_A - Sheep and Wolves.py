import sys

f = open('01_A - Sheep and Wolves.txt', 'r')
sys.stdin = f

s, w = map(int, input().split(' '))
result = 'unsafe' if w >= s else 'safe'
print(result)