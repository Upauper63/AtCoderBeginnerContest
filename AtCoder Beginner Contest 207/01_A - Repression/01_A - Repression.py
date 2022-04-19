import sys
f = open('01_A - Repression.txt', 'r')
sys.stdin = f

ls = list(map(int, input().split(' ')))
ls.sort(reverse=True)
print(sum(ls[:2]))