
import sys
f = open('02_B - Product Max.txt', 'r')
sys.stdin = f

a, b, c, d = map(int, input().split(' '))
print(max(a * c, a * d, b * c, b * d))