import sys

f = open('02_B - ROT N.txt', 'r')
sys.stdin = f

N = int(input())
S = list(input())
for i in range(len(S)):
    index = ((ord(S[i]) + N) - 65) % 26 + 65
    print(chr(index), sep='', end='')
