import sys
f = open('A - Yay!.txt', 'r')
sys.stdin = f

s = input()
for i, v in enumerate(s):
    if s[i] != s[i + 1] and s[i] != s[i + 2]:
        print(i + 1)
        exit()
    if s[i + 1] != s[i] and s[i + 1] != s[i + 2]:
        print(i + 2)
        exit()
    if s[i + 2] != s[i] and s[i + 2] != s[i + 1]:
        print(i + 3)
        exit()