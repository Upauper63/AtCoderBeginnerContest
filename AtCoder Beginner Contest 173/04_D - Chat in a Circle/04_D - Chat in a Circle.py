import sys
import os
f = open('04_D - Chat in a Circle.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
ls = ls + ls
ls.sort(reverse=True)
rst = 0
for i in range(1, N):
    rst += ls[i]
print(rst)