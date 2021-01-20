import os
import sys
f = open('04_D - Sum of Divisors.txt', 'r')
sys.stdin = f

N = int(input())
rst = 0
for i in range(1, N + 1):
    t = N // i
    rst += (i + i * t) * t // 2
print(rst)