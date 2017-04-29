
#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


graphs = {(0,1):(1,5),(0,2):(1,3),
          (1,3):(2,1),(1,4):(2,3),(1,5):(2,6),(2,4):(2,8),(2,5):(2,7),(2,6):(2,6),
          (3,7):(3,6),(3,8):(3,8),(4,7):(3,3),(4,8):(3,5),(5,8):(3,3),(5,9):(3,3),(6,8):(3,8),(6,9):(3,4),
          (7,10):(4,2),(7,11):(4,2),(8,11):(4,1),(8,12):(4,2),(9,11):(4,3),(9,12):(4,3),
          (10,13):(5,3),(10,14):(5,5),(11,13):(5,5),(11,14):(5,2),(12,13):(5,6),(12,14):(5,6),
          (13,15):(6,4),(14,15):(6,3)}


PATH = []
import sys
def RECURSIVE_SHORTEST_GRAPHS(graphs,j):
    if j == 0:
        return 0
    m = sys.maxint
    for k in range(j):
        if (graphs.has_key((k,j))):
            p = RECURSIVE_SHORTEST_GRAPHS(graphs,k)+graphs[(k,j)][1]
            if p < m:
                m = p
                s[j] = (k,j)
    return m



s = [0]*16
print "the least cost of the path is:",RECURSIVE_SHORTEST_GRAPHS(graphs,15)
#print s

#i = 15
#print s[i][1]
#j = s[i][0]
#print j
#i = s[j][0]
#print i
#j = s[i][0]
#print j
#i = s[j][0]
#print i
#j = s[i][0]
#print j
#i = s[j][0]
#print i
print "the path is:",
i =15
print s[i][1],
while s[i][0] != 0:
    j = s[i][0]
    print j,
    i = j
print s[i][0]
