import sys
f = open('03_C - Secret Number.txt', 'r')
sys.stdin = f

s = input()
rst = 0

def check(val):
    if val < 1000:
        if not (s[0] == 'o' or s[0] == '?'):
            return False
        else:
            val = str(val)
            val = '0' * (4 - len(val)) + val
    for k, v in enumerate(s):
        if v == 'o' and str(k) not in str(val):
            return False
        if v == 'x' and str(k) in str(val):
            return False
    return True

for i in range(10000):
    if check(i):
        rst += 1
print(rst)