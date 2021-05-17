import sys
f = open('03_C - Bowls and Dishes.txt', 'r')
sys.stdin = f

def int_minusone(x):
    return int(x) - 1

n, m = map(int, input().split(' '))
condi = []
val = 0
for _ in range(m):
    a, b = map(int_minusone, input().split(' '))
    condi.append((a, b))
k = int(input())
people = []
for _ in range(k):
    c, d = map(int_minusone, input().split(' '))
    people.append((c, d))
for i in range(1 << k):
    tmp_val = 0
    dishes = [0 for i in range(n)]
    for j in range(k):
        if i >> j & 1:
            dishes[people[j][0]] = 1
        else:
            dishes[people[j][1]] = 1
    for a, b in condi:
        if dishes[a] & dishes[b]:
            tmp_val += 1
    val = max(tmp_val, val)
print(val)