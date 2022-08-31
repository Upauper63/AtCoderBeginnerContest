import sys
from xml.dom import InuseAttributeErr
f = open('A - "atcoder".substr().txt', 'r')
sys.stdin = f

l, r = map(int, input().split(' '))
s = "atcoder"
print(s[l-1:r])