import sys
f = open('C - ±1 Operation 1.txt', 'r')
sys.stdin = f

x, a, d, n = map(int, input().split(' '))
ls_min = min(a, a + (n - 1) * d)
ls_max = max(a, a + (n - 1) * d)
if x <= ls_min:
    print(ls_min - x)
elif x >= ls_max:
    print(x - ls_max)
else:
    k = (x - a) // d
    print(min(abs((a + k * d) - x), abs((a + (k + 1) * d) - x)))