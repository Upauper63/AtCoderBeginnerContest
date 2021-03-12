
import sys
f = open('03_C - Repsept.txt', 'r')
sys.stdin = f

K = int(input())
cnt = 1
val = 7

for i in range(K):
    val %= K
    if val == 0:
        print(cnt)
        exit()
    else:
        val = val * 10 + 7
        cnt += 1
print(-1)