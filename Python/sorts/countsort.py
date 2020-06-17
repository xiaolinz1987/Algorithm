class MyCountSort:

    def __init__(self, input_array):
        self.array = input_array
        self.sorted_array = []
    
    def reset(self, input_array):
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

    def count_sort_v2(self):
        max_value = self.array[0]
        min_value = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] > max_value:
                max_value = self.array[i]
            if self.array[i] < min_value:
                min_value = self.array[i]

        d = max_value - min_value
        count_array = [0] * (d+1)
        for i in range(0, len(self.array)):
            count_array[self.array[i] - min_value] += 1
        
        for i in range(1, len(self.array)):
            count_array[i] += count_array[i-1]

        self.sorted_array = [9] * len(self.array)
        for i in range(len(self.array)-1, -1, -1):
            self.sorted_array[count_array[self.array[i] - min_value] - 1] = self.array[i]
            count_array[self.array[i] - min_value] -= 1

    def get_array(self):
        return self.sorted_array

