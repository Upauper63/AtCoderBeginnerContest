import sys
f = open('02_B - Magic 3.txt', 'r')
sys.stdin = f

n, s, d = map(int, input().split(' '))
for i in range(n):
    x, y = map(int, input().split(' '))
    if x < s and y > d:
        print('Yes')
        exit()
print('No')