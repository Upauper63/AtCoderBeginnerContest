import sys
f = open('B - Modulo Number.txt', 'r')
sys.stdin = f

n = int(input())
print(n % 998244353)