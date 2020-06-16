class MyPriorityQueue:

    def __init__(self):
        self.array = []
        self.size = 0
    
    def __up_adjust(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) // 2
        temp = self.array[child_index]
        
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (parent_index - 1) // 2
        
        self.array[child_index] = temp

    def __down_adjust(self):
        child_index = 1
        parent_index = 0
        temp = self.array[parent_index]
        
        while child_index < self.size:
            if child_index + 1 < self.size and self.array[child_index + 1] > self.array[child_index]:
                child_index += 1
            
            if temp >= self.array[child_index]:
                break
            
            self.array[parent_index] = self.array[child_index]
            parent_index = child_index
            child_index = child_index * 2 + 1
        
        self.array[parent_index] = temp

    def enqueue(self, element):
        self.array.append(element)
        self.size += 1
        self.__up_adjust()

    def dequeue(self):
        if self.size < 0:
            raise Exception("Empty queue!")
        head = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.__down_adjust()
        return head

