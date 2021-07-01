import sys
f = open('04_D - Megalomania.txt', 'r')
sys.stdin = f

n = int(input())
condi = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    condi.append((a, b))
condi = sorted(condi, key=lambda x: x[1])
val = 0
for k, v in condi:
    val += k
    if val > v:
        print('No')
        exit()
print('Yes')