import sys
f = open('C - Cards Query Problem.txt', 'r')
sys.stdin = f

n = int(input())
q = int(input())
ls = [[] for _ in range(n)]
dic = {}
for _ in range(q):
    query = list(map(int, input().split(' ')))
    if query[0] == 1:
        ls[query[2] - 1].append(query[1])
        if not query[1] in dic:
            dic[query[1]] = {query[2]}
        else:
            dic[query[1]].add(query[2])
    if query[0] == 2:
        ls[query[1] - 1].sort()
        print(' '.join(map(str, ls[query[1] - 1])))
    if query[0] == 3:
        tmp = sorted(dic[query[1]])
        print(' '.join(map(str, tmp)))