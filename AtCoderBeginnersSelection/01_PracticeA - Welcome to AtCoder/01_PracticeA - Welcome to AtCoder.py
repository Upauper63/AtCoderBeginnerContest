import sys
import os
f = open('01_PracticeA - Welcome to AtCoder.txt', 'r')
sys.stdin = f

a = int(input())
b, c = map(int, input().split(' '))
s = input()

print("{} {}".format(a+b+c, s))