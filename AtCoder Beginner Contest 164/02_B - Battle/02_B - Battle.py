import sys

f = open('02_B - Battle.txt', 'r')
sys.stdin = f

turn = "A"
A, B, C, D = map(int, input().split(' '))

def Attack(hp, damage):
    hp -= damage
    return hp


while A > 0 and B > 0:
    if turn == "A":
        C = Attack(C, B)
        turn = "C"
        if not C > 0:
            print('Yes')
            break
    else:
        A = Attack(A, D)
        turn = "A"
        if not A > 0:
            print('No')
            break
