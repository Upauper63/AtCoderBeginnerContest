import sys

f = open('01_A - Blackjack.txt', 'r')
sys.stdin = f

ls = list(map(int, input().split(' ')))
if sum(ls) >= 22:
    print('bust')
else:
    print('win')