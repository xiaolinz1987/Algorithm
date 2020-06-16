class MyHeap:

    def __init__(self, input_list):
        self.list = input_list

    def reset_input(self, input_list):
        self.list = input_list

    def up_adjust(self):
        child_index = len(self.list) - 1
        parent_index = (child_index - 1) // 2
        temp = self.list[child_index]
        while child_index > 0 and temp < self.list[parent_index]:
            self.list[child_index] = self.list[parent_index]
            child_index = parent_index
            parent_index = (parent_index - 1) // 2
        self.list[child_index] = temp

    def down_adjust(self, parent_index, length):
        temp = self.list[parent_index]
        child_index = parent_index * 2 + 1
        while child_index < length:
            if child_index + 1 < length and self.list[child_index + 1] < self.list[child_index]:
                child_index += 1
            if temp <= self.list[child_index]:
                break
            self.list[parent_index] = self.list[child_index]
            parent_index = child_index
            child_index = child_index * 2 + 1
        self.list[parent_index] = temp

    def build(self):
        for i in range((len(self.list)-2) // 2, -1, -1):
            self.down_adjust(i, len(self.list))

    def get_heap(self):
        return self.list

input = list([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
myHeap = MyHeap(input)
myHeap.up_adjust()
print(myHeap.get_heap())
input = list([7, 1, 3, 10, 5, 2, 8, 9, 6])
myHeap.reset_input(input)
myHeap.build()
print(myHeap.get_heap())

