import sys
f = open('C - LRUD Instructions 2.txt', 'r')
sys.stdin = f

n = int(input())
s = list(input())
trace = set()
trace.add((0, 0))
tmp_x = 0
tmp_y = 0

def check(tmp_x, tmp_y):
    if (tmp_x, tmp_y) in trace:
        print('Yes')
        exit()

for i in s:
    if i == 'U':
        tmp_y += 1
        check(tmp_x, tmp_y)
        trace.add((tmp_x, tmp_y))
    if i == 'R':
        tmp_x += 1
        check(tmp_x, tmp_y)
        trace.add((tmp_x, tmp_y))
    if i == 'D':
        tmp_y -= 1
        check(tmp_x, tmp_y)
        trace.add((tmp_x, tmp_y))
    if i == 'L':
        tmp_x -= 1
        check(tmp_x, tmp_y)
        trace.add((tmp_x, tmp_y))
print('No')