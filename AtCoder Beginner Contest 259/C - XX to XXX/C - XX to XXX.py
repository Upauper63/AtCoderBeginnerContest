import sys
f = open('C - XX to XXX.txt', 'r')
sys.stdin = f

s = input()
t = input()

def check_data(val):
    idx = 0
    data = {}
    tmp = ''
    for v in val:
        if tmp != v:
            tmp = v
            idx += 1
            data[v + str(idx)] = 1
        else:
            data[tmp + str(idx)] += 1
    return data

s_data = check_data(s)
t_data = check_data(t)
is_ok = True
for k, v in t_data.items():
    if not (k in s_data):
        is_ok = False
        break
    if v == 1 and s_data[k] >= 2:
        is_ok = False
        break
    if v >= 2 and s_data[k] == 1:
        is_ok = False
        break
    if v < s_data[k]:
        is_ok = False
        break
if is_ok:
    print('Yes')
else:
    print('No')