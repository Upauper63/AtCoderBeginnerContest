
import sys
f = open('01_A - Star.txt', 'r')
sys.stdin = f

X = int(input()) % 100
print(100 - X)
