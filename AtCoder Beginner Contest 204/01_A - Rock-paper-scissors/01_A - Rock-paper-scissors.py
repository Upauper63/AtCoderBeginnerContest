import sys
f = open('01_A - Rock-paper-scissors.txt', 'r')
sys.stdin = f

x, y = map(int, input().split(' '))
choices = [0, 1, 2]
if x == y:
    print(x)
else:
    choices.remove(x)
    choices.remove(y)
    print(choices[0])