my_list = [3, 1, 2, 5, 4, 9, 7, 2]
#print(my_list[2])
#print(my_list[3])

my_list[3] = 10
#print(my_list[3])

#print(my_list)
my_list.append(6)
my_list.insert(5, 11)
#print(my_list)

class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert_v1(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("Out of range!")

        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]

        self.array[index] = element
        self.size += 1

    def insert_v2(self, index, element):
        if index < 0 or index > self.size:
            raise Exception("Out of range")

        if self.size >= len(self.array):
            self.resize()

        for i in range(self.size-1, -1, -1):
            self.array[i+1] = self.array[i]

        self.array[index] = element
        self.size += 1

    def resize(self):
        array_new = [None] * len(self.array) * 2
        for i in range(self.size):
            array_new[i] = self.array[i]
        self.array = array_new

    def output(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

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



