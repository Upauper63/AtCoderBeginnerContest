import sys
f = open('D - Count Subtractions.txt', 'r')
sys.stdin = f

a, b = map(int, input().split(' '))
is_end = False
cnt = 0
while not is_end:
    if a > b:
        cnt += a // b
        a = a % b
    else:
        cnt += b // a
        b = b % a
    if a == 0 or b == 0:
        is_end = True
        cnt -= 1
print(cnt)