import sys

f = open('01_A - Calc.txt', 'r')
sys.stdin = f

a = int(input())
print(a + a**2 + a**3)