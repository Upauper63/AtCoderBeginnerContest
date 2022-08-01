import sys
f = open('A - When?.txt', 'r')
sys.stdin = f

k = int(input())
print(str(21 + k // 60) + ':' + (str(k % 60)).zfill(2))