class MyCountSort:

    def __init__(self, input_array):
        self.array = input_array
        self.sorted_array = []

    def count_sort_v1(self):
        max_value = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] > max_value:
                max_value = self.array[i]

        count_array = [0] * (max_value + 1)
        for i in range(0, len(self.array)):
            count_array[self.array[i]] += 1

        for i in range(0, len(count_array)):
            for j in range(0, count_array[i]):
                self.sorted_array.append(i)

    def output(self):
        print(self.sorted_array)

input = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10])
sort = MyCountSort(input)
sort.count_sort_v1()
print("count_sort_v1:")
sort.output()

