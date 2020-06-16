class MyArray:

    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0
        self.result = []

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
        self.result = []
        for i in range(self.size):
            self.result.append(self.array[i])

    def get_array(self):
        self.output()
        return self.result

