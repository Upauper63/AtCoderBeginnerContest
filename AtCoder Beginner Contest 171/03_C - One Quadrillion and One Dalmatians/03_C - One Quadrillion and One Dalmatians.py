
import sys
f = open('03_C - One Quadrillion and One Dalmatians.txt', 'r')
sys.stdin = f

n = int(input())
n-=1

for l in range(1,15):
    if n >= 26 ** l:        
        n -= 26 ** l
        continue

    ans = ""
    for i in range(l):
        d = n % 26
        ans += chr(d + ord('a'))
        n //= 26
    ans = ans[::-1]
    break
print(ans)