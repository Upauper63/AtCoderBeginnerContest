import sys
import os
f = open('04_.txt', 'r')
sys.stdin = f

n = int(input())
nums = list(map(int, input().split(' ')))
nums.sort(reverse=True)
ls = [0] * n
for i in range(1,n):
    ls[i] = nums[i-1]
print(sum(ls))