class MyArray:

    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def __assert_index(self, index):
        if index < 0 or index > self.size:
            raise Exception("Out of range")

    def __insert(self, index, element):
        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def insert_v1(self, index, element):
        self.__assert_index(index)
        self.__insert(index, element)

    def insert_v2(self, index, element):
        self.__assert_index(index)
        if self.size >= len(self.array):
            self.resize()
        self.__insert(index, element)

    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def remove(self, index):
        self.__assert_index(index)
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def output(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

"""
array = MyArray(4)
array.insert_v1(0, 10)
array.output()
array.insert_v1(0, 11)
array.output()
array.insert_v1(0, 15)
array.output()
array.insert_v1(0, 20)
array.output()
array.insert_v2(0, 29)
array.output()
array.insert_v2(0, 32)
array.output()
array.insert_v2(0, 41)
array.output()
array.insert_v2(0, 58)
array.output()
array.remove(1)
array.output()
"""
