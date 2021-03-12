import sys

f = open('02_B - Palindrome-philia.txt', 'r')
sys.stdin = f

S = input()
cnt = 0
for i in range(len(S) // 2):
    if S[i] != S[-i-1]:
        cnt += 1
print(cnt)