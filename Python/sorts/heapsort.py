import sys
sys.path.append('../')
from utils.heap import MyHeap

class MyHeapSort:

    def __init__(self, input_array):
        self.array = input_array
        self.heap = MyHeap(self.array)

    def heap_sort(self):
        self.heap.build()
        
        for i in range(len(self.array)-1, 0, -1):
            temp = self.array[i]
            self.array[i] = self.array[0]
            self.array[0] = temp
            self.heap.down_adjust(0, i)

    def output(self):
        print(self.array)

"""
input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
sort = MyHeapSort(input)
sort.heap_sort()
sort.output()
"""
