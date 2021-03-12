import sys

f = open('02_B - YYMM or MMYY.txt', 'r')
sys.stdin = f

S = input()
if 0 < int(S[:2]) < 13 and 0 < int(S[2:]) < 13:
    print('AMBIGUOUS')
elif 0 < int(S[:2]) < 13:
    print('MMYY')
elif 0 < int(S[2:]) < 13:
    print('YYMM')
else:
    print('NA')