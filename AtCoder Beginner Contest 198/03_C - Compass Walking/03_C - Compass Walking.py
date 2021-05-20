import sys
f = open('03_C - Compass Walking.txt', 'r')
sys.stdin = f

import math
r, x, y = map(int, input().split(' '))
if math.sqrt(x ** 2 + y ** 2) % r == 0:
    print(int(math.sqrt(x ** 2 + y ** 2) // r))
elif math.sqrt(x ** 2 + y ** 2) < r:
    print(2)
else:
    print(int(math.sqrt(x ** 2 + y ** 2) // r) + 1)

