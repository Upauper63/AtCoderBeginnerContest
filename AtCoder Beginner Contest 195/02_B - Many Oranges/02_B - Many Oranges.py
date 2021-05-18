import sys
f = open('02_B - Many Oranges.txt', 'r')
sys.stdin = f

a, b, w = map(int, input().split(' '))
w *= 1000

max_num = 0
min_num = float('inf')

for i in range(1, w + 1):
    if a * i <= w <= b * i:
        if min_num == float('inf'):
            min_num = i
        max_num = i
if max_num:
    print(min_num, max_num)
else:
    print('UNSATISFIABLE')