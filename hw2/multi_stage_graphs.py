#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com

A = [(0,1,5),(0,2,3),
        (1,3,1),(1,4,3),(1,5,6),(2,4,8),(2,5,7),(2,6,6),
        (3,7,6),(3,8,8),(4,7,2),(4,8,5),(5,8,3),(5,9,3),(6,8,8),(6,9,4),
        (7,10,2),(7,11,2),(8,11,1),(8,12,2),(9,11,3),(9,12,3),
        (10,13,3),(10,14,5),(11,13,5),(11,14,2),(12,13,6),(12,14,6),
        (13,15,4),(14,15,3)]
import sys
def printnode(s,end):
    if s[end] == 0:
        print end,"==>"
        return
    printnode(s,s[end])
    print end,"==>"

def printpath(s,length):
    print s[0],"==>"
    printnode(s,length-1)
    print "shortest path"


B = [sys.maxint for i in range(16)]
S = [0 for i in range(16)]
B[0] = 0
for i in range(len(A)):
    B[A[i][1]] = A[i][2] + B[A[i][0]]
    S[A[i][1]] = A[i][0]
print S
print B
printpath(S,15)
