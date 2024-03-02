import sys
f = open('B - Which is ahead?.txt', 'r')
sys.stdin = f

n = int(input())
p_ls = list(input().split(' '))
q = int(input())
for i in range(q):
    a, b = input().split(' ')
    a_cnt = p_ls.index(a)
    b_cnt = p_ls.index(b)
    if a_cnt < b_cnt:
        print(a)
    else:
        print(b)