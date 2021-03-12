import sys

f = open('01_A - Remaining Balls.txt', 'r')
sys.stdin = f

dict = {}
S, T = input().split(' ')
dict[S], dict[T] = map(int, input().split(' '))
U = input()
dict[U] -= 1
print(dict[S], dict[T])

