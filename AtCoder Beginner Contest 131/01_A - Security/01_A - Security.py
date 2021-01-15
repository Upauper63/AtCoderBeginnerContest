import sys
import os
f = open('01_A - Security.txt', 'r')
sys.stdin = f

result = 'Good'
S = list(input())
for i in range(len(S) - 1):
    if S[i] == S[i+1]:
        result = 'Bad'
print(result)