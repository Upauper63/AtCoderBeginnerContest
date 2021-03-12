import sys

f = open('02_B - Count ABC.txt', 'r')
sys.stdin = f

N = int(input())
S = input()
print(S.count('ABC'))
