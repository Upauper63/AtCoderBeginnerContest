import sys
f = open('01_A - Tiny Arithmetic Sequence.txt', 'r')
sys.stdin = f

a_ls = list(map(int, input().split(' ')))
a_ls.sort()
a1, a2, a3 = a_ls
if (a3 - a2) == (a2 - a1):
    print('Yes')
else:
    print('No')