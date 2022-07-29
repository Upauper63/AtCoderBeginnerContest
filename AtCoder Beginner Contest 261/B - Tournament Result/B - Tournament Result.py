import sys
f = open('B - Tournament Result.txt', 'r')
sys.stdin = f

n = int(input())
ls = [[] for i in range(n)]
for i in range(n):
    tmp = list(input())
    for v in tmp:
        if v == 'W':
            ls[i].append(1)
        elif v == 'L':
            ls[i].append(-1)
        else:
            ls[i].append(0)
is_ok = True
for i in range(n):
    if not is_ok:
        break
    for j in range(i + 1, n):
        if ls[i][j] + ls[j][i]:
            is_ok = False
            break
if is_ok:
    print('correct')
else:
    print('incorrect')