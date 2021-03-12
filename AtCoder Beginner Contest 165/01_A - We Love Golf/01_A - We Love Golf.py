import sys

f = open('01_A - We Love Golf.txt', 'r')
sys.stdin = f

k = int(input())
a, b = map(int, input().split(' '))
result = 'NG'
for i in range(a, b + 1):
    if i % k == 0:
        result = 'OK'
print(result)