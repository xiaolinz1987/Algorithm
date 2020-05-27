class MyQuickSort:

    def __init__(self, input_array):
        self.array = input_array

    def reset_input(self, input_array):
        self.array = input_array

    def __partition_v1(self, start_index, end_index):
        pivot = self.array[start_index]
        left = start_index
        right = end_index

        while left != right:
            while left < right and self.array[right] > pivot:
                right -= 1
            while left < right and self.array[left] <= pivot:
                left += 1

            if left < right:
                temp = self.array[left]
                self.array[left] = self.array[right]
                self.array[right] = temp

        self.array[start_index] = self.array[left]
        self.array[left] = pivot
        return left
    
    def __quick_sort_core(self, start_index, end_index):
        if start_index >= end_index:
            return
        pivot_index = self.__partition_v1(start_index, end_index)
        self.__quick_sort_core(start_index, pivot_index - 1)
        self.__quick_sort_core(pivot_index + 1, end_index)

    def quick_sort(self):
        self.__quick_sort_core(0, len(self.array)-1)

    def output(self):
        print(self.array)

input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
sort = MyQuickSort(input)
sort.quick_sort()
print("quick_sort v1:")
sort.output()

