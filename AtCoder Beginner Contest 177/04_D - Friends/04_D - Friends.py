
import sys
f = open('04_D - Friends.txt', 'r')
sys.stdin = f

N, M = map(int, input().split(' '))
class UnionFind():
    def __init__(self, n):
        self.parents = [-1 for i in range(n)]

    def find(self, i):
        if self.parents[i] < 0:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return
        
        if self.parents[i] > self.parents[j]:
            j, i = i, j
        
        self.parents[i] += self.parents[j]
        self.parents[j] = i

    def size(self, i):
        return -self.parents[self.find(i)]

def int_minus_one(X):
    return int(X) - 1

uf = UnionFind(N)

for i in range(M):
    a, b = map(int_minus_one, input().split(' '))
    uf.union(a, b)

rst = 0
for i in range(N):
    rst = max(rst, uf.size(i))
print(rst)