#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com


def max_sum(p):
    sum = p[0]
    result = p[0]
    start = 0
    for i in range(1,len(p)-1):
        if sum > 0:
            sum += p[i]
        else:
            sum = p[i]
            start = i
        if sum > result:
            result = sum
            end = i
    return result,start,end

p = [-2,11,-4,13,-5,-2]
result,start,end = max_sum(p)
print result
print p[start:end+1]
