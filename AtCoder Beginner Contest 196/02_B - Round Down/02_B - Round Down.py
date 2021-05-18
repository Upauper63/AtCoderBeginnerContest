import sys
f = open('02_B - Round Down.txt', 'r')
sys.stdin = f

x = input()
idx = x.find('.')
if idx > 0:
    print(x[:idx])
else:
    print(x)