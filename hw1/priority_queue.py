#Author：康赣鹏
#
#StudentID：14130140377
#
#Email：1159838847@qq.com

class MaxHeap:
    def __init__(self,item=[]):
        self.items = item
        self.HeapLength = len(self.items)

    def PARENT(self,i):
        return i/2

    def LEFT(self,i):
        return 2*i

    def RIGHT(self,i):
        return 2*i+1

    def MAX_HEAPIFY(self,i):
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.HeapLength and self.items[l] > self.items[i]:
            largest = l
        else:
            largest = i

        if r < self.HeapLength and self.items[r] > self.items[largest]:
            largest = r

        if largest != i:
            self.items[i],self.items[largest] = self.items[largest],self.items[i]
            self.MAX_HEAPIFY(largest)

    def BUILD_MAX_HEAP(self):
        i = self.PARENT(len(self.items)-1)
        while i >= 0:
            self.MAX_HEAPIFY(i)
            i = i - 1

    def HEAP_EXTRACT_MAX(self):
        temp = len(self.items) - 1
        if temp < 0:
            return False
        else:
            self.items[0],self.items[temp] = self.items[temp],self.items[0]
            val = self.items.pop()
            self.HeapLength -= 1
            self.MAX_HEAPIFY(0)
            return val


    def MAX_HEAP_INSERT(self,key):
        #if key < self.items[self.HeapLength]:
            #return False
        self.items.append(key)
        i = len(self.items) - 1
        parId = self.PARENT(i)
        while i >= 0 and self.items[parId] < self.items[i]:
            self.items[parId],self.items[i] = self.items[i],self.items[parId]
            i = parId
            parId = self.PARENT(parId)

        self.HeapLength = self.HeapLength + 1

    def SHOW(self):
        print self.items


class PRIORITY_QUEUE(MaxHeap):
    def __init__(self,item = []):
        MaxHeap.__init__(self,item)

    def EnQueue(self,key):
        MaxHeap.MAX_HEAP_INSERT(self,key)

    def DeQueue(self):
        val = MaxHeap.HEAP_EXTRACT_MAX(self)
        return val



s = [2,4,6,3,6,9,5,2,4,7,6,4,9,2,9]
p = PRIORITY_QUEUE()
i = len(s)-1

for j in range(i):
    p.EnQueue(s[j])
    p.SHOW()

for j in range(i):
    p.DeQueue();
    p.SHOW()
