
import sys
f = open('03_C - Multiplication 3.txt', 'r')
sys.stdin = f

# a,b = map(float, input().split(' '))
# ans = (int(a) * int(b *100))
# print(type(ans))
a,b = input().split(' ')
a = int(a)
b = int(b.replace('.', ''))
ans = a * b // 100
print(ans)