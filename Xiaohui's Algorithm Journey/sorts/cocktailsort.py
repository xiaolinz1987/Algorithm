class MyCockTailSort:

    def __init__(self, input_array):
        self.array = input_array

    def cock_tail_sort(self):
        for i in range(len(self.array)-1):
            is_sorted = True
            for j in range(i, len(self.array)-i-1):
                if self.array[j] > self.array[j+1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp
                    is_sorted = False

            if is_sorted:
                break

            is_sorted = True
            for j in range(len(self.array)-i-1, i, -1):
                if self.array[j] < self.array[j-1]:
                    temp = self.array[j]
                    self.array[j] = self.array[j-1]
                    self.array[j-1] = temp
                    is_sorted = False

            if is_sorted:
                break
    
    def output(self):
        print(self.array)

input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
sort = MyCockTailSort(input)
sort.cock_tail_sort()
sort.output()

