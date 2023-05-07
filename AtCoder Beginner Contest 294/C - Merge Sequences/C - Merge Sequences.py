import sys
f = open('C - Merge Sequences.txt', 'r')
sys.stdin = f

n, m = map(int, input().split(' '))
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
a_cnt_ls = []
b_cnt_ls = []
cnt = 1
while a_ls or b_ls:
    if a_ls and b_ls:
        if a_ls[0] < b_ls[0]:
            a_ls.pop(0)
            a_cnt_ls.append(cnt)
        else:
            b_ls.pop(0)
            b_cnt_ls.append(cnt)
    elif a_ls:
        a_ls.pop(0)
        a_cnt_ls.append(cnt)
    else:
        b_ls.pop(0)
        b_cnt_ls.append(cnt)
    cnt += 1
print(' '.join(map(str, a_cnt_ls)))
print(' '.join(map(str, b_cnt_ls)))
