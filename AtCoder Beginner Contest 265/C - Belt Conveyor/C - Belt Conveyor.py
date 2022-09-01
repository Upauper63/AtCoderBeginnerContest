import sys
f = open('C - Belt Conveyor.txt', 'r')
sys.stdin = f

h, w = map(int, input().split(' '))
maze = [list(input()) for i in range(h)]
tmp = [0, 0]
rut = [[False] * w for i in range(h)]
rut[0][0] = True
def move(v, tmp):
    is_end = False
    if v == 'U':
        if tmp[0] - 1 < 0:
            is_end = True
            return [tmp, is_end]
        else:
            return [[tmp[0]-1, tmp[1]], is_end]
    if v == 'D':
        if tmp[0] + 1 >= h:
            is_end = True
            return [tmp, is_end]
        else:
            return [[tmp[0]+1, tmp[1]], is_end]
    if v == 'L':
        if tmp[1] - 1 < 0:
            is_end = True
            return [tmp, is_end]
        else:
            return [[tmp[0], tmp[1] - 1], is_end]
    if v == 'R':
        if tmp[1] + 1 >= w:
            is_end = True
            return [tmp, is_end]
        else:
            return [[tmp[0], tmp[1] + 1], is_end]
is_end = False
while not is_end:
    tmp, is_end = move(maze[tmp[0]][tmp[1]], tmp)
    if not is_end and rut[tmp[0]][tmp[1]]:
        print(-1)
        exit()
    rut[tmp[0]][tmp[1]] = True

print(tmp[0] + 1, tmp[1] + 1)