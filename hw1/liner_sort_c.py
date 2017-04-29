
#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


#c.the algorithm which satisfies criteria 2 and 3
#the algorithm is stable
#the algorithm sorts in place,using no more than a constant
#amount of storge space in addition to the original array
s = [0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,0]

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

print ("c:",merge_sort(s))
