import sys
f = open('04_D - Poker.txt', 'r')
sys.stdin = f

k = int(input())
s = input()
t = input()
s_ls = [0] * 9
t_ls = [0] * 9
sum_ls = [0] * 9
cnt = 0
val = 0
for i, j in zip(s[:-1], t[:-1]):
    i = int(i) - 1
    j = int(j) - 1
    s_ls[i] += 1
    t_ls[j] += 1
    sum_ls[i] += 1
    sum_ls[j] += 1
for i in range(9):
    s_ls[i] += 1
    s_pat = k - sum_ls[i]
    sum_ls[i] += 1
    if sum_ls[i] <= k:
        for j in range(9):
            t_ls[j] += 1
            t_pat = k - sum_ls[j]
            sum_ls[j] += 1
            if sum_ls[j] <= k:
                s_val = 0
                for m, n in enumerate(s_ls):
                    s_val += (m + 1) * 10 ** n
                t_val = 0
                for m, n in enumerate(t_ls):
                    t_val += (m + 1) * 10 ** n
                if s_val > t_val:
                    val += s_pat * t_pat
            t_ls[j] -= 1
            sum_ls[j] -= 1
    s_ls[i] -= 1
    sum_ls[i] -= 1
print(val / ((9 * k - 8) * (9 * k - 9)))