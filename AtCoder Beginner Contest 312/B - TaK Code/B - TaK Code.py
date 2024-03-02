import sys
f = open('B - TaK Code.txt', 'r')
sys.stdin = f

n, m = map(int, input().split(' '))
maze = []
for i in range(n):
    maze.append(input())
def Check(i, j):
    global n, m, maze
    if i + 8 > n or j + 8 > m:
        return False
    for s in range(i, i + 3):
        if  '.' in maze[s][j:j+3]:
            return False
        if '#' == maze[s][j+3]:
            return False
    if '#' in maze[i+3][j : j+4]:
        return False
    for s in range(i+6, i+9):
        if  '.' in maze[s][j+6 : j+9]:
            return False
        if '#' == maze[s][j+5]:
            return False
    if '#' in maze[i+5][j+5 : j+9]:
        return False
    return True
        
for i in range(n):
    for j in range(m):
        if Check(i, j):
            print(i+1, j+1)