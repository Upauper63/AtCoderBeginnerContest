import sys
f = open('04_D - Disjoint Set of Common Divisors.txt', 'r')
sys.stdin = f

import math
a, b = map(int, input().split(' '))
ab_gcd = math.gcd(a, b)
ab_cd = set()
ab_cd.add(1)
while ab_gcd % 2 == 0:
    ab_cd.add(2)
    ab_gcd //= 2
i = 3
while i * i <= ab_gcd:
    if ab_gcd % i == 0:
        ab_cd.add(i)
        ab_gcd //= i
    else:
        i += 2
if ab_gcd != 1:
    ab_cd.add(ab_gcd)
print(len(ab_cd))
