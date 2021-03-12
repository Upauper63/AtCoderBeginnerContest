import sys

f = open('02_B - Resistors in Parallel.txt', 'r')
sys.stdin = f

N = int(input())
A_ls = map(int, input().split(' '))
result = 0
for A in A_ls:
    result += 1 / A
print(1/result)