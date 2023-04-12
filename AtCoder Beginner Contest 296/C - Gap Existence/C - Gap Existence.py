import sys
f = open('C - Gap Existence.txt', 'r')
sys.stdin = f

n, x = map(int, input().split(' '))
a_set = set(map(int, input().split(' ')))
for ai in a_set:
    if ai + x in a_set or ai - x in a_set:
        print('Yes')
        exit()
print('No')