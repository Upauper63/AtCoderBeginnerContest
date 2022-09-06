import sys
f = open('C - Convex Quadrilateral.txt', 'r')
sys.stdin = f

p = [tuple(map(int, input().split(' '))) for i in range(4)]
def ccw(p1, p2, p3):
    x1 = p1[0] - p2[0]
    x2 = p3[0] - p2[0]
    y1 = p1[1] - p2[1]
    y2 = p3[1] - p2[1]
    return x1 * y2 - y1 * x2 < 0

for i in range(4):
    if not ccw(p[i], p[(i + 1) % 4], p[(i + 2) % 4]):
        print('No')
        exit()
print('Yes')