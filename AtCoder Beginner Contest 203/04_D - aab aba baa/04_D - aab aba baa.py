import sys
f = open('04_D - aab aba baa.txt', 'r')
sys.stdin = f

import math
a, b, k = map(int, input().split(' '))
tmp = 0
val = 0
rst = ''

def check(a, rest, tmp, rst):
    a -= 1
    if a < 0 or tmp == k:
        rst += 'b' * rest
        print(rst)
        exit()
    rest -= 1
    val = math.factorial(rest) // (math.factorial(a) * math.factorial(rest - a))

    if k > tmp + val:
        rst += 'b'
        a += 1
        tmp += val
        check(a, rest, tmp, rst)
    else:
        rst += 'a'
        check(a, rest, tmp, rst)

check(a, a + b, tmp, rst)