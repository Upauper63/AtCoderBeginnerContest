import sys
f = open('04_D - Knight.txt', 'r')
sys.stdin = f

x, y = map(int, input().split(' '))
mod = 10 ** 9 + 7
if (x + y) % 3 != 0:
    print(0)
    exit()
n = (x + y) // 3
if x < n or y < n:
    print(0)
    exit()
x -= n
y -= n
numerator, denominator_x, denominator_y = 1, 1, 1
for i in range(x + y):
    numerator *= (x + y - i) % mod
    numerator %= mod
for i in range(x):
    denominator_x *= pow(x - i, mod - 2, mod)
    denominator_x %= mod
for i in range(y):
    denominator_y *= pow(y - i, mod - 2, mod)
    denominator_y %= mod
print(numerator * denominator_x * denominator_y % mod)