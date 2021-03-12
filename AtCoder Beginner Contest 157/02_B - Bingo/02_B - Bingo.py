import sys

f = open('02_B - Bingo.txt', 'r')
sys.stdin = f

ls = []
for i in range(3):
    ls.append(list(input().split(' ')))

N = int(input())
for i in range(N):
    X = input()
    for i in range(3):
        if X in ls[i]:
            ls[i][ls[i].index(X)] = 0

result = False
for i in range(3):
    if ls[i].count(0) == 3:
        result = True
        break

if not result:
    for i in range(3):
        cnt = 0
        for j in range(3):
            if ls[j][i] == 0:
                cnt += 1
        if cnt == 3:
            result = True
            break

if not result:
    cnt = 0
    for i in range(3):
        if ls[i][i] == 0:
            cnt += 1
    if cnt == 3:
        result = True

if not result:
    cnt = 0
    for i in range(3):
        if ls[i][3-i-1] == 0:
            cnt += 1
    if cnt == 3:
        result = True

if result:
    print('Yes')
else:
    print('No')