import sys
f = open('01_A - Maxi-Buying.txt', 'r')
sys.stdin = f

n = int(input())
if n * 1.08 // 1 > 206:
    print(' :( ')
elif n * 1.08 // 1 == 206:
    print('so-so')
else:
    print('Yay! ')