objects = [0.5,0.7,0.3,0.9,0.6,0.8,0.1,0.4,0.2,0.5]

objects.sort()

left = 0
right = 9
Bin = []

while left < right :
    if objects[left] + objects[right] <= 1:
        Bin.append([objects[left],objects[right]])
        left += 1
        right -= 1
    elif objects[left] + objects[right] > 1:
        Bin.append([objects[right]])
        right -= 1

print Bin
