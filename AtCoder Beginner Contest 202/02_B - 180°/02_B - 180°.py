import sys
f = open('02_B - 180°.txt', 'r')
sys.stdin = f

s = input()
rst = ''
for i in s[::-1]:
    if i == '6':
        i = '9'
    elif i == '9':
        i = '6'
    rst += i
print(rst)