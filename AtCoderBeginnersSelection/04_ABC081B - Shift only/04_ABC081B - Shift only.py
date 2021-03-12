
import sys
f = open('04_ABC081B - Shift only.txt', 'r')
sys.stdin = f

input()
nums = map(int, input().split(' '))

cnt=0
end = False
while end!=True:
    tmp_num = []
    for num in nums:
        if num % 2 != 0:
            print(cnt)
            end = True
            break
        else:
            tmp_num.append(num / 2)
    cnt+=1
    nums = tmp_num