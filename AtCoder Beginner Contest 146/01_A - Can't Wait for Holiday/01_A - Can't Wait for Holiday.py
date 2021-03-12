import sys

f = open("01_A - Can't Wait for Holiday.txt", 'r')
sys.stdin = f

S = input()
ls = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
cnt = 0
dict = {}
for item in ls:
    dict[item] = cnt
    cnt += 1
print(7 - dict[S])