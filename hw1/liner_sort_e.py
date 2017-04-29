
#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com

#e

sford = [234,213,453,678,234,125,109,9,0,7,900,808]

def INPLACE_COUNTING_SORT(A,k):
    c =[]
    c_save = []
    n = len(A)
    for i in range(0,k+1):
        c.append(0)
        c_save.append(0)
    for j in range(0,n):
        c[A[j]] += 1
        c_save[A[j]] += 1
    for j in range(1,k+1):
        c[j] = c[j] + c[j-1]
        c_save[j] = c_save[j] + c_save[j-1]

    i = n-1
    while i >=0:
        if i>c[A[i]]-1 and i<=c_save[A[i]]-1:
            i = i - 1
        else:
            c[A[i]] = c[A[i]] - 1
            A[c[A[i]]-1],A[i] = A[i],A[c[A[i]]-1]

    return A

print ("e:",INPLACE_COUNTING_SORT(sford,max(sford)))
