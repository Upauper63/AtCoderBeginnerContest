import sys
f = open('02_B - Do you know the second highest mountain.txt', 'r')
sys.stdin = f

n = int(input())
ls = []
for _ in range(n):
    s, t = input().split(' ')
    ls.append((s, int(t)))
ls = sorted(ls, key=lambda x: x[1], reverse=True)
print(ls[1][0])