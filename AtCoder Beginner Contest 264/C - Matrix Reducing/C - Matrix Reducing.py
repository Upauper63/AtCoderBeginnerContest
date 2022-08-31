import sys
f = open('C - Matrix Reducing.txt', 'r')
sys.stdin = f

from itertools import combinations
h1, w1 = map(int, input().split(' '))
a = []
for i in range(h1):
    a.append(list(map(int, input().split(' '))))
h2, w2 = map(int, input().split(' '))
b = []
for i in range(h2):
    b.append(list(map(int, input().split(' '))))

for h in combinations([i for i in range(h1)], h2):
    for w in combinations([j for j in range(w1)], w2):
        is_ok = True
        if is_ok:
            for m, s in enumerate(h):
                if is_ok:
                    for n, t in enumerate(w):
                        if a[s][t] != b[m][n]:
                            is_ok = False
                            break
        if is_ok:
            print('Yes')
            exit()
print('No')