
import sys
f = open('01_A - Slot.txt', 'r')
sys.stdin = f

S = input()
if S[0] == S[1] == S[2]:
    print('Won')
else:
    print('Lost')