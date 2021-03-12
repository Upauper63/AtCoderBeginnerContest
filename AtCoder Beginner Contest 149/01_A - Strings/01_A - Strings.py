import sys

f = open('01_A - Strings.txt', 'r')
sys.stdin = f

S, T = input().split(' ')
print(T, S, sep="")