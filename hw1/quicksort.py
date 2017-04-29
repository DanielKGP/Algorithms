#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


def PARTITION(numlist,left,right):
    flag = numlist[right]
    i = left - 1
    for j in range(left,right):
        if numlist[j] <= flag:
            i = i + 1
            numlist[i],numlist[j]=numlist[j],numlist[i]

    numlist[right],numlist[i+1]=numlist[i+1],numlist[right]
    return i+1

def QUICKSORT(numlist,left,right):
    if left < right:
        middle = PARTITION(numlist,left,right)
        QUICKSORT(numlist,left,middle-1)
        QUICKSORT(numlist,middle+1,right)
    return numlist

s = [2,5,3,7,1,8,3,7,0,2,4,7,9]
print("before sort:",s)
s = QUICKSORT(s,left = 0,right = len(s)-1)
print("after sort:",s)
