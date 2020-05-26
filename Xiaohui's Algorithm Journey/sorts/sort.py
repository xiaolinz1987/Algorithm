class MySort:
    def __init__(self, input_array):
        self.array = input_array
    
    def bubble_sort_v1(self):
        for i in range(len(self.array)-1):
            for j in range(len(self.array)-i-1):
                if self.array[j] > self.array[j+1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp

    def output(self):
        print(self.array)

input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
sort = MySort(input)
sort.bubble_sort_v1()
sort.output()

