class MyQueue:

    def __init__(self, capacity):
        self.list = [None] * capacity
        self.front = 0
        self.end = 0
        self.queue = []

    def enqueue(self, element):
        if (self.end+1) % len(self.list) == self.front:
            raise Exception("Full queue!")
        self.list[self.end] = element
        self.end = (self.end+1) % len(self.list)

    def dequeue(self):
        if self.end == self.front:
            raise Exception("Full queue!")
        dequeue_element = self.list[self.front]
        self.front = (self.front+1) % len(self.list)
        return dequeue_element

    def __size(self):
        return abs(self.end - self.front) % len(self.list)

    def empty(self):
        if self.__size() < 1:
            return True
        return False

    def output(self):
        self.queue = []
        i = self.front
        while i != self.end:
            self.queue.append(self.list[i])
            i = (i+1) % len(self.list)
    
    def get_queue(self):
        self.output()
        return self.queue

