#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com

s = [0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,0]

def COUNTING_SORT(A,B,k):
    c = []

    for i in range(0,k+1):
        c.append(0)
    for j in range(0,len(A)):
        c[A[j]] = c[A[j]] + 1
    for j in range(1,k+1):
        c[j] = c[j] + c[j-1]
    for j in range(len(A)-1,-1,-1):
        B[c[A[j]]-1] = A[j]
        c[A[j]] = c[A[j]]-1
    return B

b = [None for i in range(len(s))]
print ("a:",COUNTING_SORT(s,b,max(s)))
