
#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


import sys

def recursive_matrix_chain(p,i,j):
    if i == j:
        return 0
    for k in range(i,j):
        q = recursive_matrix_chain(p,i,k)+recursive_matrix_chain(p,k+1,j)+p[i-1]*p[k]*p[j]
        if q<m[i][j]:
            m[i][j] = q
            s[i][j] = k
    return m[i][j]


def print_optimal_parens(s,i,j):
    if i == j:
        print 'A%d'%(i),
    else:
        print '(',
        print_optimal_parens(s,i,s[i][j])
        print_optimal_parens(s,s[i][j]+1,j)
        print ')',

p = [5,10,3,12,5,60,6]
n = len(p)-1
m = [[sys.maxint for i in range(n+1)] for j in range(n+1)]
s = [[0 for i in range(n+1)] for j in range(n+1)]
recursive_matrix_chain(p,1,n)

print_optimal_parens(s,1,n)
print '\n'


def matrix_chain(p):
    n = len(p) - 1
    m = [[0]*(n+1) for i in range(n+1)]
    s = [[0]*(n+1) for i in range(n+1)]
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j = i + l - 1
            m[i][j] = sys.maxint
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s


a = [3,5,2,1,10]
b = [2,7,3,6,10]
c = [10,3,15,12,7,2]
d = [7,2,4,15,20,5]
p = [5,10,3,12,5,60,6]

m,s = matrix_chain(a)
print a
print_optimal_parens(s,1,len(a)-1)
print '\n'

m,s = matrix_chain(b)
print b
print_optimal_parens(s,1,len(b)-1)
print '\n'

m,s = matrix_chain(c)
print c
print_optimal_parens(s,1,len(c)-1)
print '\n'

m,s = matrix_chain(d)
print d
print_optimal_parens(s,1,len(d)-1)
print '\n'

m,s = matrix_chain(p)
print p
print_optimal_parens(s,1,len(p)-1)

print '\n'
print m[1][6]
