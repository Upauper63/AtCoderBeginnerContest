import sys
f = open('01_A - Bitwise Exclusive Or.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
ls = []
while a or b:
    if (a + b) % 2:
        ls.append(1)
    else:
        ls.append(0)
    a //= 2
    b //= 2
rst = 0
for i, v in enumerate(ls):
    rst += v * 2 ** i
print(rst) 