import sys

f = open('01_A - Next Alphabet.txt', 'r')
sys.stdin = f

C = input()
print(chr(ord(C) + 1))