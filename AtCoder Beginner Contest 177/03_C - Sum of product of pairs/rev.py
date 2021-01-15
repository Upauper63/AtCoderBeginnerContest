import os
import sys
f = open('03_C - Sum of product of pairs.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
except_val = 0
for i in ls:
    except_val += i ** 2
print((sum(ls) ** 2 - except_val) // 2 % (10 ** 9 + 7))