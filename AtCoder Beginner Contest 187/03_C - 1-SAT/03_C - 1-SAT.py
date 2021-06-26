import sys
f = open('03_C - 1-SAT.txt', 'r')
sys.stdin = f

N = int(input())
ls = set()
for i in range(N):
    S = input()
    if S[0] == '!':
        if S[1:] in ls:
            print(S[1:])
            exit()
        else:
            ls.add(S)
    else:
        if ('!' + S) in ls:
            print(S)
            exit()
        else:
            ls.add(S)
print('satisfiable')