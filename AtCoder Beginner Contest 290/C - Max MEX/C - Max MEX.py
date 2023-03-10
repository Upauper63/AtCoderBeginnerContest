import sys
f = open('C - Max MEX.txt', 'r')
sys.stdin = f

n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
a_set = set(a)
a_mex = 0
for i in range(n + 1):
    if i not in a_set:
        a_mex = i
        break
print(min(a_mex, k))