
class Heap:
    """this is a max heap and will heap for a sort of max to min 
    ex.... [19,18,17,16,15,14]
    if you want a min heap just change all the ">" in the methods heapup and heapdown to a "<"
    """
    def __init__(self):
        self.stuff = []
        self.length = 0
        
        

    def contents(self):
        print(self.stuff)


    def add(self, n):
        self.length = self.length + 1
        self.stuff.append(n)

        self.heapup(n)

    def delete(self):
        output = self.stuff[0]
        self.stuff[0] = self.stuff[self.length -1]
        self.stuff = self.stuff[0:self.length -1]
        self.length -= 1

        self.heapdown(0)
        return output

    def heapup(self,int):
        elt_index = self.length -1

        while(int > self.stuff[elt_index//2]): # change this > to a < for a min heap
            self.stuff[elt_index],self.stuff[elt_index//2] = self.stuff[elt_index//2],self.stuff[elt_index]
            elt_index = elt_index//2
            

    def heapdown(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < self.length and self.stuff[left] > self.stuff[largest]: # change this > to a < for a min heap
            largest = left

        if right < self.length and self.stuff[right] > self.stuff[largest]: #change this > to a < for a min heap
            largest = right

        if largest != index:
            self.stuff[index], self.stuff[largest] = self.stuff[largest], self.stuff[index]
            self.heapdown(largest)

    def heapPop(self):
        output = self.stuff.pop(-1)
        self.length -= 1
        return output

    def heapSort(self):
        output = []
        for x in range(self.length):
            output.append(self.delete())
        return output

    


        

        



heap = Heap()

for x in range(1000):
    heap.add(x)
heap.contents()

print(heap.heapPop())

print(heap.heapSort())

