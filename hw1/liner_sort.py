#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


s = [0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,0]

sford = [234,213,453,678,234,125,109,9,0,7,900,808]

#b
def liner_sort(numlist):
    left = 0
    right = len(numlist) - 1
    while left < right:
        if numlist[left] <  numlist[right]:
            left += 1
            right -= 1
        if numlist[left] > numlist[right]:
            numlist[left],numlist[right] = numlist[right],numlist[left]
            left += 1
            right -= 1
        if numlist[left] == numlist[right]:
            if numlist[left] == 1:
                right -= 1
            elif numlist[right] == 0:
                left += 1
    return numlist
#c.the algorithm which satisfies criteria 2 and 3
#the algorithm is stable
#the algorithm sorts in place,using no more than a constant
#amount of storge space in addition to the original array
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def merge_sort(numlist):
    if len(numlist) <= 1:
        return numlist
    middle = len(numlist)/2
    left = merge_sort(numlist[:middle])
    right = merge_sort(numlist[middle:])
    return merge(left, right)


#a
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

#e
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

class num:
    number = 0;
    def __init__(self,key):
        self.number = key
    def get_number(self):
        return self.number
    def get_tag(self,x):
        tag = self.number/(10**(x-1))%10
        return tag

x = num(109)
print(x.get_number(),x.get_tag(1))

#print ("d:",RADIX_SORT(s))


b = [None for i in range(len(s))]
print ("a:",COUNTING_SORT(s,b,max(s)))
print ("b:",liner_sort(s))
print ("c:",merge_sort(s))
print ("d:",RADIX_SORT())
print ("e:",INPLACE_COUNTING_SORT(sford,max(sford)))
