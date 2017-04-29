#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


s = [0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,0]

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

print ("b:",liner_sort(s))
