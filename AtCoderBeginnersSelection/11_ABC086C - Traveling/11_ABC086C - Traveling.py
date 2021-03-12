import sys

f = open('11_ABC086C - Traveling.txt', 'r')
sys.stdin = f

n = int(input())
result = "Yes"
for i in range(n):
    t, x, y = map(int, input().split(' '))
    if t >= (x + y) and (t - (x + y)) % 2 == 0:
        continue
    else:
        result = "No"
print(result)