import sys

f = open('02_B - Guidebook.txt', 'r')
sys.stdin = f

SP_list = []
N = int(input())

for i in range(N):
    items = input().split(' ')
    SP_list.append([i+1, items[0], int(items[1])])

SP_list.sort(key=lambda i:i[2], reverse=True)
SP_list.sort(key=lambda i:i[1])

for i in SP_list:
    print(i[0])