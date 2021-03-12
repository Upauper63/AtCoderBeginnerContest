import sys

f = open('01_A - Station and Bus.txt', 'r')
sys.stdin = f

S = input()
if S[0] != S[1] or S[0] != S[2]:
    print('Yes')
else:
    print('No')