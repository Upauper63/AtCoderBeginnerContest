import sys
import os
f = open('02_B - I miss you.txt', 'r')
sys.stdin = f

S = input()
Ans = ''
for i in range(len(S)):
    Ans += 'x'
print(Ans)