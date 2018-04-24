#Author:DanielKGP
#
#StudentID:14130140377
#
#Email:1159838847@qq.com

def LCStr(a,b):
    n = len(a)
    m = len(b)

    c = [([0] * (m + 1)) for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if (a[i] == b[j]):
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = 0
    return c

def get_max(c):
    coordinate = []
    max = 0
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if c[i][j] > max:
                max = c[i][j]
            else:
                pass
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if c[i][j] == max:
                coordinate.append((i,j))
    return max,coordinate


def get_lss(c,a,x,max):
    temp = []
    while max > 0:
        temp.append(a[x])
        x -= 1
        max -= 1
    lss = temp[::-1]
    return lss

a = "abcdefg"
b = "abcefg"

c = LCStr(a,b)

max,coordinate = get_max(c)
print coordinate
tempcoo = coordinate.pop()
tempcoor = coordinate.pop()

temp = get_lss(c,a,tempcoo[0],max)
print "".join(temp)

temp1 = get_lss(c,a,tempcoor[0],max)
print "".join(temp1)
