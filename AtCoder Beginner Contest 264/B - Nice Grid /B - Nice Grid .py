import sys
f = open('B - Nice Grid .txt', 'r')
sys.stdin = f

r, c = map(int, input().split(' '))
maze = [[] for i in range(15)]
for i in range(8):
    if i % 2 == 0:
        tmp = [1] * 15
        for j in range(15):
            if j % 2 == 1 and (j < i + 1 or j >= 14 - i):
                tmp[j] = 0
    else:
        tmp = [0] * 15
        for j in range(15):
            if j % 2 == 0 and (j < i + 1 or j >= 14 - i):
                tmp[j] = 1
    maze[i] = tmp
    maze[14 - i] = tmp
print('black' if maze[r - 1][c - 1] else 'white')