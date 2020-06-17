import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
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

    def get_array(self):
        return self.array

