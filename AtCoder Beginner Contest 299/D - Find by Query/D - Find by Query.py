import sys
f = open('D - Find by Query.txt', 'r')
sys.stdin = f


n = int(input())
l = 0
r = n
is_end = False
while not is_end:
    center = (l + r) // 2
    print('? ' + str(center))
    sn = int(input())
    if sn == 1:
        r = center
    else:
        l = center
    if l + 1 == r:
        print('! ' + str(l))
        is_end = True