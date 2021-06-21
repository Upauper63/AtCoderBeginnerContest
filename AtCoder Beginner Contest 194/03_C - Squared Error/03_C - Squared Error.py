import sys
f = open('03_C - Squared Error.txt', 'r')
sys.stdin = f

N = int(input())
ls = list(map(int, input().split(' ')))
except_val = 0
for i in ls:
    except_val += i ** 2
val_sq = [i ** 2 for i in ls]
val_mlt = (sum(ls) ** 2 - except_val) // 2
print((N - 1) * sum(val_sq) - 2 * val_mlt)
