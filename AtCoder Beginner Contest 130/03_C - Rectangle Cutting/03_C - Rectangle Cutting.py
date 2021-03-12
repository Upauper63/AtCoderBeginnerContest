
import sys
f = open('03_C - Rectangle Cutting.txt', 'r')
sys.stdin = f

W, H, x, y = map(int, input().split(' '))
is_var = 1 if W / 2 == x and H / 2 == y else 0
print(W * H / 2, is_var)