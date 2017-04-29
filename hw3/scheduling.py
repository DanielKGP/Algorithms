import sys

jobs = [15,8,3,10]
num = len(jobs)
sche = []
leasttime = 0.0
def ExtractMin(jobs,num):
    minint = min(jobs)
    for i in range(len(jobs)):
        if jobs[i] == minint:
            temp = i
            jobs[i] = sys.maxint
    num -= 1
    return temp,num,minint

def scheduling(jobs,num,leasttime):
    while num > 0:
        temp,num,minint = ExtractMin(jobs,num)
        sche.append(temp)
        leasttime += minint*(num+1)
    return num,leasttime

num,leasttime = scheduling(jobs,num,leasttime)
print "the scheduling squence is : ",sche
print "the least average completion time is : ",leasttime/len(jobs)
