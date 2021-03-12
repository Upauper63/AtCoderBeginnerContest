import sys

f = open('02_B - Papers, Please.txt', 'r')
sys.stdin = f

N = input()
A_ls = map(int, input().split(' '))
A_ls = [i for i in A_ls if i % 2 == 0]
ls = [i for i in A_ls if i % 3 == 0 or i % 5 == 0]
if len(A_ls) == len(ls):
    print('APPROVED')
else:
    print('DENIED')