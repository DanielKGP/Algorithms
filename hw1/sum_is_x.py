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

def sum(numlist,x):
    right = 0
    left = len(numlist) - 1
    while right < left:
        if numlist[right] + numlist[left] == x:
            return (right,left)
        elif numlist[right] + numlist[left] < x:
            right = right + 1
        else:
            left = left - 1
    return False

print(sum(s,11))
