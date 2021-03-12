import sys

f = open('02_B - String Palindrome.txt', 'r')
sys.stdin = f

def CheckPalindrome(S, L):
    result = True
    for i in range((L+1)//2):
        if S[i] != S[-i-1]:
            result = False
            break
    return result

result = True
S = input()
L = len(S)

result = CheckPalindrome(S, L)

if result:
    S2 = S[:(len(S)-1) // 2]
    L2 = len(S2)
    result = CheckPalindrome(S2, L2)

if result:
    S3 = S[(L+3)//2-1:]
    L3 = len(S3)
    result = CheckPalindrome(S3, L3)

if result:
    print('Yes')
else:
    print('No')