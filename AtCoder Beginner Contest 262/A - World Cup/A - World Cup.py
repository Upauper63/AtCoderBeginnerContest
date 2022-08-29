import sys
f = open('A - World Cup.txt', 'r')
sys.stdin = f

y = int(input())
while y % 4 != 2:
    y += 1
print(y)