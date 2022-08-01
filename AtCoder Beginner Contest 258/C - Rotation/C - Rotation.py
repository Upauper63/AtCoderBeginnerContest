import sys
f = open('C - Rotation.txt', 'r')
sys.stdin = f

n, q = map(int, input().split(' '))
s = input()
diff = 0
for i in range(q):
    t, x = map(int, input().split(' '))
    if t - 1:
        print(s[(x + diff - 1) % n])
    else:
        diff -= x