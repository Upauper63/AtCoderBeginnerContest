import os
import sys
f = open('04_D - Bouquet.txt', 'r')
sys.stdin = f

n, a, b = map(int, input().split(' '))
mod = 10 ** 9 + 7
rst = pow(2, n, mod) - 1
a_val, b_val = 1, 1
for i in range(a):
    a_val *= (n - i) * pow(i + 1, mod - 2, mod)
    a_val %= mod
for i in range(b):
    b_val *= (n - i) * pow(i + 1, mod - 2, mod)
    b_val %= mod
rst = (rst - a_val - b_val) % mod
print(rst)