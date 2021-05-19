import sys
f = open('02_B - Visibility.txt', 'r')
sys.stdin = f

h, w, y, x = map(int, input().split(' '))
x -= 1
y -= 1
maze = []
for _ in range(h):
    maze.append(list(input()))
rst = 1
i = -1
while y + i >= 0:
    if maze[y + i][x] == '#':
        break
    if maze[y + i][x] == '.':
        rst += 1
    i -= 1
i = 1
while y + i < h:
    if maze[y + i][x] == '#':
        break
    if maze[y + i][x] == '.':
        rst += 1
    i += 1
i = -1
while x + i >= 0:
    if maze[y][x + i] == '#':
        break
    if maze[y][x + i] == '.':
        rst += 1
    i -= 1
i = 1
while x + i < w:
    if maze[y][x + i] == '#':
        break
    if maze[y][x + i] == '.':
        rst += 1
    i += 1
print(rst)