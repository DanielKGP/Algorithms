def MeanValues(weight,values,number):
    res = [-1.0 for i in range(number)]
    for i in range(number):
        res[i] = values[i]/weight[i]
    return res

def ExtractMax(mean,number):
    Maxmean = max(mean)
    for i in range(number):
        if mean[i] == Maxmean:
            temp = i
            mean[i] = -1.0
    return mean,temp


def Fractinalknapsack(capacity,mean,number,weight,mostvalues):
    while capacity > 0:
        if max(mean) > 0:
            mean,temp = ExtractMax(mean,number)
            if capacity >= weight[temp]:
                capacity -= weight[temp]
                weight[temp] = 0
                mostvalues += values[temp]
                valueslist.append(temp)
            elif capacity < weight[temp]:
                i = weight[temp]
                fractional = capacity/i
                mostvalues += fractional*values[temp]
                valueslist.append(temp)
                capacity = 0
    print valueslist
    print "the last value's fraction :",fractional
    print "the most values :",mostvalues

number=5
capacity=100
weight=[50.0,30.0,45.0,25.0,5.0]
values=[200.0,180.0,225.0,200.0,50.0]
valueslist = []
mostvalues = 0.0


mean = MeanValues(weight,values,number)
Fractinalknapsack(capacity,mean,number,weight,mostvalues)
