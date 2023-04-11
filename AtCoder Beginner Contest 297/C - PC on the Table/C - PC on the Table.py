import sys
f = open('C - PC on the Table.txt', 'r')
sys.stdin = f

h, w = map(int, input().split(' '))
maze = []
for i in range(h):
    maze.append(list(input()))
for r in maze:
    for j in range(w - 1):
        if r[j] == r[j + 1] == 'T':
            r[j] = 'P'
            r[j + 1] = 'C'
for r in maze:
    print(''.join(r))