import sys
import os
f = open('02_B - Golden Coins.txt', 'r')
sys.stdin = f

X = int(input())
print(X // 500 * 1000 + (X % 500) // 5 * 5)