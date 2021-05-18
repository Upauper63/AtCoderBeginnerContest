import sys
f = open('03_C - Comma.txt', 'r')
sys.stdin = f

n = input()
if len(n) <= 3:
    print(0)
    exit()
rst = 0
cnt = (len(n) - 1) // 3
for i in range(cnt):
    rst += i * ((10 ** (3 * (i + 1)) - 1) - (10 ** (3 * i) - 1))
rst += cnt * (int(n) - (10 ** (3 * cnt) - 1))
print(rst)