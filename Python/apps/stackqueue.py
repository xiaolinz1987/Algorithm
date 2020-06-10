class MyStackQueue:

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def enqueue(self, element):
        self.stack_a.append(element)

    def __transfer(self):
        while len(self.stack_a) > 0:
            self.stack_b.append(self.stack_a.pop())

    def dequeue(self):
        if len(self.stack_b) == 0:
            if len(self.stack_a) == 0:
                raise Exception("Empty queue!")
            
            self.__transfer()
        return self.stack_b.pop()

queue = MyStackQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())

