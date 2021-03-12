import sys

f = open('02_B - FizzBuzz Sum.txt', 'r')
sys.stdin = f

N = int(input())
result = 0
for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        result += i
print(result)