import os
import sys
f = open('03_C - Go to School.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
dic = {}
for idx, val in enumerate(ls):
    dic[val] = idx
dic = sorted(dic.items())
for i in dic:
    print(i[1] + 1, end=' ')