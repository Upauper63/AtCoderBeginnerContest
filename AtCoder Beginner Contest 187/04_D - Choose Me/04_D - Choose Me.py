import sys
f = open('04_D - Choose Me.txt', 'r')
sys.stdin = f

N = int(input())
loss = []
A_sum = 0
B_sum = 0
for i in range(N):
    A, B = map(int, input().split(' '))
    loss.append(A * 2 + B)
    A_sum += A
loss.sort(reverse=True)
cnt = 0
while A_sum >= B_sum:
    B_sum += loss[cnt]
    cnt += 1
print(cnt)
