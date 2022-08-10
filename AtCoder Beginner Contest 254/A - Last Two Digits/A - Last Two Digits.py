import sys
f = open('A - Last Two Digits.txt', 'r')
sys.stdin = f

n = int(input())
print(str(n % 100).zfill(2))