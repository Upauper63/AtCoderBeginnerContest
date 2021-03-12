import sys

f = open('01_A - Weather Prediction.txt', 'r')
sys.stdin = f

S = input()
ls = ['Sunny', 'Cloudy', 'Rainy']
index = (ls.index(S) + 1) % 3
print(ls[index])