import sys

f = open('06_ABC083B - Some Sums.txt', 'r')
sys.stdin = f

max_num, a, b = map(int, input().split(' '))
num = 0
ans_sum = 0
while num <= max_num:
    str_num = str(num)
    digit_nums = list(str_num)
    digit_sum = 0
    for digit_num in digit_nums:
        digit_sum += int(digit_num)
    if a <= digit_sum <= b:
        ans_sum += num
    num += 1

print(ans_sum)