import sys
f = open('C - Dango.txt', 'r')
sys.stdin = f

n = int(input())
s = input()
s_alt = s.split('-')
s_alt_len = list(map(len, s_alt))
x = max(s_alt_len)
if 0 < x < n:
    print(x)
else:
    print(-1)