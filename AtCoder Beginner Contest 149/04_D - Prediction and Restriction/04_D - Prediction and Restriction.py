import sys
f = open('04_D - Prediction and Restriction.txt', 'r')
sys.stdin = f

N, K = map(int, input().split(' '))
R, S, P = map(int, input().split(' '))
T = input()

rst = 0
dic = {'r':P, 's':R, 'p':S}
cnt = [0] * K
for idx, val in enumerate(T):
    if cnt[idx % K] == 0 or T[idx] != T[idx - K]:
        rst += dic[val]
        cnt[idx % K] = dic[val]
    else:
        cnt[idx % K] = 0
print(rst)