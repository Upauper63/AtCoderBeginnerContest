import sys
import os
f = open('01_A - Lucky 7.txt', 'r')
sys.stdin = f

result = 'Yes' if input().count('7') > 0 else 'No'
print(result)