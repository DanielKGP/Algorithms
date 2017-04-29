#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


def RECURSIVE_LCS(x,y):
    if (len(x) == 0 or len(y) == 0):
        return 0
    else:
        a = x[0]
        b = y[0]
        if (a == b):
            listc.append(a)
            return RECURSIVE_LCS(x[1:],y[1:]) + 1
        else:
            return MAX_SE(RECURSIVE_LCS(x[1:],y),RECURSIVE_LCS(x,y[1:]))

def MAX_SE(a,b):
    if(a >= b):
        return a
    else:
        return b

a = "xzyzzyx"
b = "zxyyzxz"
lista =  []
listb =  []
listc =  []
for i in range(0, len(a)):
    lista.append(a[i])
for i in range(0, len(b)):
    listb.append(b[i])

len = RECURSIVE_LCS(lista,listb)
print len
