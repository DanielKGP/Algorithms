#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com

def RECURSIVE_LCStr(x,y):
    if (len(x) == 0 or len(y) == 0):
        return 0
    else:
        a = x[0]
        b = y[0]
        if (a == b):
            return RECURSIVE_LCStr(x[1:],y[1:])+1
        else:
            return 0

temp = []
cxStra = "baacbad"
cxStrb = "bacba"
lista = []
listb = []

for i in range(0, len(cxStra) ):
    lista.append(cxStra[i])
for  i in range(0, len(cxStrb)):
    listb.append(cxStrb[i])

#while lenLSS < 11:
lenLSS = RECURSIVE_LCStr(lista, listb)

print('LSS Length is:{0}', lenLSS)
