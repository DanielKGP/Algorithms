import sys

graph = [[0,1,3,6],
         [1,0,1,5],
         [3,1,0,2],
         [6,5,2,0]]

n = 4
d = [0,sys.maxint,sys.maxint,sys.maxint]
p = [-1,-1,-1,-1]

def relax(a,b):
    if(d[b] > d[a] + graph[a][b]):
        d[b] = d[a] + graph[a][b]

for k in range(n-1):
    for i in range(n):
        for j in range(n):
            relax(i,j)
print d
