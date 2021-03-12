import sys

f = open('03_C - Maximum Volume.txt', 'r')
sys.stdin = f

L = int(input())
print((L/3)**3)