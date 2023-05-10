import sys
f = open('C - Make Takahashi Happy.txt', 'r')
sys.stdin = f

h, w = map(int, input().split(' '))
cnt = 0
maze = []
for i in range(h):
    maze.append(list(map(int, input().split(' '))))

def check(y, x, route):
    global cnt
    if maze[y][x] in route:
        return
    if y == h - 1 and x == w - 1:
        cnt += 1
        route = []
        return
    route.append(maze[y][x])
    if y < h - 1:
        check(y + 1, x, route)
    if x < w - 1:
        check(y, x + 1, route)
    route.pop(-1)
    
check(0, 0, [])
print(cnt)
