import sys

f = open('01_A - Circle.txt', 'r')
sys.stdin = f

r = int(input())
print(r ** 2)