
import sys
f = open('03_C - Super Ryuma.txt', 'r')
sys.stdin = f

def check(a, b, c, d):
    if a + b == c + d: return True
    if a - b == c - d: return True
    if abs(a - c) + abs(b - d) <= 3: return True
    return False

r1, c1 = map(int, input().split(' '))
r2, c2 = map(int, input().split(' '))

if r1 == r2 and c1 == c2:
    print(0)
    exit()

if check(r1, c1, r2, c2):
    print(1)
    exit()

if (r1 + c1) % 2 == (r2 + c2) % 2:
    print(2)
    exit()

for i in range(-3, 4):
    for j in range(-3, 4):
        if abs(i) + abs(j) > 3:
            continue
        r_tmp = r1 + i
        c_tmp = c1 + j
        if check(r1, c1, r_tmp, c_tmp) and check(r_tmp, c_tmp, r2, c2):
            print(2)
            exit()

print(3)
