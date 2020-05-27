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
    
    def __quick_sort_core_v1(self, start_index, end_index):
        if start_index >= end_index:
            return
        pivot_index = self.__partition_v1(start_index, end_index)
        self.__quick_sort_core_v1(start_index, pivot_index - 1)
        self.__quick_sort_core_v1(pivot_index + 1, end_index)

    def __partition_v2(self, start_index, end_index):
        pivot = self.array[start_index]
        mark = start_index

        for i in range(start_index+1, end_index+1):
            if self.array[i] < pivot:
                mark += 1
                temp = self.array[mark]
                self.array[mark] = self.array[i]
                self.array[i] = temp

        self.array[start_index] = self.array[mark]
        self.array[mark] = pivot
        return mark

    def __quick_sort_core_v2(self, start_index, end_index):
        if start_index >= end_index:
            return
        pivot_index = self.__partition_v2(start_index, end_index)
        self.__quick_sort_core_v2(start_index, pivot_index - 1)
        self.__quick_sort_core_v2(pivot_index + 1, end_index)

    def quick_sort_v1(self):
        self.__quick_sort_core_v1(0, len(self.array)-1)

    def quick_sort_v2(self):
        self.__quick_sort_core_v2(0, len(self.array)-1)

    def output(self):
        print(self.array)

input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
sort = MyQuickSort(input)
sort.quick_sort_v1()
print("quick_sort_v1:")
sort.output()
sort.reset_input(input)
sort.quick_sort_v2()
print("quick_sort_v2:")
sort.output()
