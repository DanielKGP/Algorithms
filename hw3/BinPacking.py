
#Author:kangganpeng
#
#StudentID:14130140377
#
#Email:1159838847@qq.com


objects = [0.5,0.7,0.3,0.9,0.6,0.8,0.1,0.4,0.2,0.5]

objects.sort()

left = 0
right = 9
Bin = []
Bin.append([])
Bincount = 0

while left < right :
    if objects[left]+objects[right] + sum(Bin[Bincount]) <= 1:
        Bin[Bincount].append(objects[left])
        Bin[Bincount].append(objects[right])
        left += 1
        right -= 1
    elif objects[left]+sum(Bin[Bincount]) <= 1:
        Bin[Bincount].append(objects[left])
        left += 1
    elif objects[right]+sum(Bin[Bincount]) <= 1:
        Bin[Bincount].append(objects[right])
        right -= 1
    else:
        Bin.append([])
        Bincount += 1

print Bin
