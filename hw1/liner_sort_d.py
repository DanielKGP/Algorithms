
#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com

#d
import random
def RADIX_SORT():
    A = [random.randint(1,99) for i in xrange(100)]
    for k in xrange(2):
        s = [[]for i in xrange(10)]
        for i in A:
            s[i/(10**k)%10].append(i)
        A = [a for b in s for a in b]
    return A


print ("d:",RADIX_SORT())
