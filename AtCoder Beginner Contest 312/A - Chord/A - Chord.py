import sys
f = open('A - Chord.txt', 'r')
sys.stdin = f

s = input()
ls = ['ACE', 'BDF', 'CEG', 'DFA', 'EGB', 'FAC', 'GBD']
if s in ls:
    print('Yes')
else:
    print('No')