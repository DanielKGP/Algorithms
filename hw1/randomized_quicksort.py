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
            temp = numlist[i]
            numlist[i] = numlist[j]
            numlist[j] = temp
    temp = numlist[right]
    numlist[right] = numlist[i+1]
    numlist[i+1] = temp

    return i+1

import random

def RANDOMIZED_PARTITION(numlist,left,right):
    #print(left,right)
    templeft = left
    tempright = right
    i = random.randint(templeft,tempright)
    #print(i )
    #print('\n')
    tmp = numlist[i]
    numlist[i] = numlist[right]
    numlist[right] = tmp

    return PARTITION(numlist,left,right)


def RANDOMIZED_QUICKSORT(numlist,left,right):
    if left < right:
        middle = RANDOMIZED_PARTITION(numlist,left,right)
        RANDOMIZED_QUICKSORT(numlist,left,middle-1)
        RANDOMIZED_QUICKSORT(numlist,middle+1,right)
    return numlist

s = [2,5,3,7,1,8,3,7,0,2,4,7,9]
print("before sort:",s)
s = RANDOMIZED_QUICKSORT(s,left = 0,right = len(s)-1)
print("after sort:",s)
