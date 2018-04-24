bestV=0
currentW=0
currentV=0
bestx=None

def backtrack_knapsack(i):
    global bestV,currentW,currentV,x,bestx
    if i>=n:
        if bestV<currentV:
            bestV=currentV
            bestx=x[:]
    else:
        if currentW+w[i]<=c:
            x[i]=1
            currentW+=w[i]
            currentV+=v[i]
            backtrack_knapsack(i+1)
            currentW-=w[i]
            currentV-=v[i]
        x[i]=0
        backtrack_knapsack(i+1)

n=5
c=10
w=[1,2,3,6,4]
v=[2,3,5,4,9]
x=[0 for i in range(n)]
backtrack_knapsack(0)
print "the largest value is:",(bestV)
print(bestx)
