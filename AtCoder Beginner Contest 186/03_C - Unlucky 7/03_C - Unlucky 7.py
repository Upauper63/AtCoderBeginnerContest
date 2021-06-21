
import sys
f = open('03_C - Unlucky 7.txt', 'r')
sys.stdin = f

N = int(input())
ls = []
excep_cnt = 0
for i in range(1, N + 1):
    oct_i = oct(i)
    if '7' in str(oct_i) or '7' in str(i):
        excep_cnt += 1
print(N - excep_cnt)