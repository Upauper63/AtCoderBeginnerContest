from ast import operator
import sys
f = open('B - Better Students Are Needed!.txt', 'r')
sys.stdin = f

import operator
n, x, y, z = map(int, input().split(' '))
data = [{'idx': i,  'math': 0, 'eng': 0, 'sum': 0} for i in range(n)]
res = []
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
for i in range(n):
    data[i]['math'] = a_ls[i]
    data[i]['eng'] = b_ls[i]
    data[i]['sum'] = a_ls[i] + b_ls[i]
data = sorted(data, key=operator.itemgetter('math'), reverse=True)
for i in range(x):
    res.append(data[0]['idx'])
    data.pop(0)
data = sorted(data, key=operator.itemgetter('idx'))
data = sorted(data, key=operator.itemgetter('eng'), reverse=True)
for i in range(y):
    res.append(data[0]['idx'])
    data.pop(0)
data = sorted(data, key=operator.itemgetter('idx'))
data = sorted(data, key=operator.itemgetter('sum'), reverse=True)
for i in range(z):
    res.append(data[0]['idx'])
    data.pop(0)    
[ print(i + 1) for i in sorted(res) ]