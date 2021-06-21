
import sys
f = open('01_A - Discount.txt', 'r')
sys.stdin = f

A, B = map(int, input().split(' '))
print((A - B) / A * 100)