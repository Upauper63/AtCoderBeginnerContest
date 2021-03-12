import sys

f = open('07_ABC088B - Card Game for Two.txt', 'r')
sys.stdin = f

input()
nums = list(map(int,input().split(' ')))
nums.sort(reverse=True)

print(sum(nums[::2])-sum(nums[1::2]))