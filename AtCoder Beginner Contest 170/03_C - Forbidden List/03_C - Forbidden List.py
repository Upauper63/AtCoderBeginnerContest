
import sys
f = open('03_C - Forbidden List.txt', 'r')
sys.stdin = f

x, n = map(int, input().split(' '))
min_num = 100

ls = [0] * 201
for i in range(0, 201):
    ls[i] = i

ls_in = [0] * n
if n > 0:
    ls_in = list(map(int, input().split(' ')))
    for i in ls_in:
        ls.remove(i)
    ls.reverse()
    for i in ls:
        min_num = min(abs(x-i), min_num)
        if abs(x-i) == min_num:
            ans = i 
    print(ans)
else:
    print(x)