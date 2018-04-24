#Author:kangganpeng
#
#StudentID:14130140377
#
#Email:1159838847@qq.com

def knapsack(number,capacity,weight,values):
    res=[[0 for j in range(capacity+1)] for i in range(number+1)]
    for j in range(capacity+1):
        res[0][j]=0
    for i in range(1,number+1):
        for j in range(1,capacity+1):
            res[i][j]=res[i-1][j]
            if j>=weight[i-1] and res[i][j]<res[i-1][j-weight[i-1]]+values[i-1]:
                res[i][j]=res[i-1][j-weight[i-1]]+values[i-1]
    return res

def show(number,capacity,weight,res):
    print 'the largest value:',res[number][capacity]
    x=[False for i in range(number)]
    j=capacity
    for i in range(number,0,-1):
        if res[i][j]>res[i-1][j]:
            x[i-1]=True
            j-=weight[i-1]
    for i in range(number):
        if x[i] == True:
            print 'No ',i+1

number=5
capacity=100
weight=[50,30,45,25,5]
values=[200,180,225,200,50]
res=knapsack(number,capacity,weight,values)
show(number,capacity,weight,res)
