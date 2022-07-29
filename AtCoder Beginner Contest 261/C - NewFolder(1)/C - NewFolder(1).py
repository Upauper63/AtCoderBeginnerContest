import sys
f = open('C - NewFolder(1).txt', 'r')
sys.stdin = f

n = int(input())
ls = [input() for i in range(n)]
counter = {}
print(ls[0])
counter[ls[0]] = 1
for i in range(1, n):
    if ls[i] in counter:
        print(ls[i] + '(' + str(counter[ls[i]]) + ')')
        counter[ls[i]] += 1
    else:
        print(ls[i])
        counter[ls[i]] = 1
        