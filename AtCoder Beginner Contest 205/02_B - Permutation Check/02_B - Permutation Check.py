import sys
f = open('02_B - Permutation Check.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
a_ls.sort()
for k, v in enumerate(a_ls):
    if k + 1 != v:
        print('No')
        exit()
print('Yes')