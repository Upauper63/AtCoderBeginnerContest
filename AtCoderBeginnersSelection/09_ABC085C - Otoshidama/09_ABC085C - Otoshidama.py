import sys

f = open('09_ABC085C - Otoshidama.txt', 'r')
sys.stdin = f

num, price = map(int, input().split(' '))
end = False
for i in range(num+1):
    for j in range(num+1 - i):
        if 10000 * (num - i -j) + 5000 * i + 1000 * j == price:
            end = True
            break
    if end:
        break
if end:
    print("{} {} {}".format((num-i-j), i, j))
else:
    print("-1 -1 -1")
