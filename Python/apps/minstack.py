class MyMinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, element):
        self.main_stack.append(element)

        if len(self.min_stack) == 0 or element <= self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(element)

    def pop(self):
        if self.main_stack[len(self.main_stack)-1] == self.min_stack[len(self.min_stack)-1]:
            self.min_stack.pop()

        return self.main_stack.pop()

    def get_min(self):
        if len(self.min_stack) == 0:
            return None

        return self.min_stack[len(self.min_stack)-1]

stack = MyMinStack()
stack.push(4)
stack.push(9)
stack.push(7)
stack.push(3)
stack.push(8)
stack.push(5)
print(stack.get_min())
stack.pop()
stack.pop()
stack.pop()
print(stack.get_min())
