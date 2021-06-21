
import sys
f = open('02_B - uNrEaDaBlE sTrInG.txt', 'r')
sys.stdin = f

S = input()
is_dif = True
for idx, chr in enumerate(S):
    if idx % 2:
        if ord(chr) >= ord('a'):
            is_dif = False
            break
    else:
        if ord(chr) < ord('a'):
            is_dif = False
            break
if is_dif:
    print('Yes')
else:
    print('No')