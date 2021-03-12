
import sys
f = open('04_D - Caracal vs Monster.txt', 'r')
sys.stdin = f

import math
H = int(input())
n = math.floor(math.log2(H)) + 1
print(2 ** n - 1)