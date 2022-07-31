import sys
f = open('C - XX to XXX.txt', 'r')
sys.stdin = f

s = input()
t = input()
s_new = ''
for idx, v in enumerate(s):
    if idx <= len(s) - 3 and v == s[idx + 1] and v == s[idx + 2]:
        tmp = ''
    else:
        tmp = v
    s_new += tmp
t_new = ''
for idx, v in enumerate(t):
    if idx <= len(t) - 3 and v == t[idx + 1] and v == t[idx + 2]:
        tmp = ''
    else:
        tmp = v
    t_new += tmp
print(s_new)
if s_new == t_new:
    print('Yes')
else:
    print('No')