import sys
f = open('02_B - Palindrome with leading zeros.txt', 'r')
sys.stdin = f

n = input()
idx = 0
for i in n[::-1]:
    if i == '0':
        idx += 1
    else:
        break

n = n[:len(n) - idx]
for i in range(len(n) // 2):
    if n[i] != n[- i - 1]:
        print('No')
        exit()
print('Yes')