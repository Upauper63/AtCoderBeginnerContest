import sys
f = open('04_D - Journey.txt', 'r')
sys.stdin = f

from decimal import Decimal
n = int(input())
rst = 0
for i in range(1, n):
    rst += n / i 
print(rst)