class BinaryHeap():
    def __init__(self, list = None):
        self.data = []
        self.treeLenght = 0
        if(list is not None):
            self.data = list
            self.treeLenght = len(list) - 1
            self.__heapify()
    
    def __get_children_indexes(self, index):
        return [index * 2 + 1, index * 2 + 2] 
    
    def __get_parent_index(self, index):
        if (index % 2 == 1):
            return (index - 1) // 2
        else:
            return (index - 2) // 2
    
    def __sift_up(self, index):
        while True:
            parent = self.__get_parent_index(index)
            if (index == 0):
                break
            elif (self.data[parent] < self.data[index]):
                self.data[parent], self.data[index] = self.data[index], self.data[parent]
                index = parent
            else:
                break
    
    def __sift_down(self, index):
        while True:
            changeIndex = index
            children = self.__get_children_indexes(index)

            if ((children[0] < self.treeLenght) and (self.data[children[0]] > self.data[changeIndex])):
                changeIndex = children[0]
            if ((children[1] < self.treeLenght) and (self.data[children[1]] > self.data[changeIndex])):
                changeIndex = children[1]

            if (changeIndex != index):
                self.data.append(5)
                self.data[index], self.data[changeIndex] = self.data[changeIndex], self.data[index]
                index = changeIndex
            else:
                break
    
    def __heapify(self):
        for index in range(0, self.treeLenght + 1):
            self.__sift_up(index)

    def extract_max(self, deleteMax = True):
        toReturnNum = self.data[0]
        self.data[self.treeLenght], self.data[0] = self.data[0], self.data[self.treeLenght]
        if (deleteMax):
            self.data.pop()
        self.treeLenght -= 1
        self.__sift_down(0)
        return toReturnNum
    
    def add(self, number):
        currentIndex = self.treeLenght + 1
        self.treeLenght += 1
        self.data.append(number)
        self.__sift_up(currentIndex)


def heap_sort(list):
    binaryHeap = BinaryHeap(list)
    for i in range(0, binaryHeap.treeLenght + 1):
        binaryHeap.extract_max(deleteMax=False)

def is_binary_heap(list):
    for i in range(len(list) - 1, 0, -1):
        parentIndex = (i - 1) // 2
        if (list[i] > list[parentIndex]):
            return False
    return True
