class MyQueue:

    def __init__(self, capacity):
        self.list = [None] * capacity
        self.front = 0
        self.end = 0

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
        i = self.front
        while i != self.end:
            print(self.list[i], end = ' ')
            i = (i+1) % len(self.list)
        print()

myQueue = MyQueue(6)
myQueue.enqueue(3)
myQueue.output()
myQueue.enqueue(5)
myQueue.output()
myQueue.enqueue(6)
myQueue.output()
myQueue.dequeue()
myQueue.output()
myQueue.dequeue()
myQueue.output()
myQueue.enqueue(2)
myQueue.output()
myQueue.enqueue(4)
myQueue.output()

