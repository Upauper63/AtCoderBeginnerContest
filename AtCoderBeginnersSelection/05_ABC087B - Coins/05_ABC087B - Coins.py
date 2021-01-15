import os
import sys
f = open('05_ABC087B - Coins.txt', 'r')
sys.stdin = f

a = int(input())
b = int(input())
c = int(input())
price = int(input())

cnt = 0
a_tmp = a
while a_tmp >= 0:
    b_tmp = b
    if a_tmp * 500 > price:
        a_tmp -=1
        continue
    while b_tmp >= 0:
        c_tmp = c
        if b_tmp * 100 > price:
            b_tmp -=1
            continue
        while c_tmp >= 0:
            if a_tmp * 500 + b_tmp * 100 + c_tmp * 50 == price:
                cnt += 1
            c_tmp -= 1
        b_tmp -= 1        
    a_tmp -= 1

print(cnt)