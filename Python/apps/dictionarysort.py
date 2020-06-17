class MyDictionarySort:

    def __init__(self, input_array):
        self.array = input_array
        self.border_index = 0
        self.result = []

    def reset(self, input_array):
        self.array = input_array
        self.border_index = 0

    def __find_swap_border(self):
        for i in range(len(self.array)-1, 0, -1):
            if self.array[i] > self.array[i-1]:
                self.border_index = i
                return

    def __swap(self):
        head = self.array[self.border_index - 1]
        for i in range(len(self.array)-1, 0, -1):
            if head < self.array[i]:
                self.array[self.border_index - 1] = self.array[i]
                self.array[i] = head
                break

    def __reverse(self):
        i = self.border_index
        j = len(self.array) - 1
        while i < j:
            temp = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = temp
            i += 1
            j -= 1

    def sort(self):
        self.__find_swap_border()
        if self.border_index == 0:
            return

        self.__swap()
        self.__reverse()

    def output(self):
        self.result = []
        for i in self.array:
            self.result.append(i)
    
    def get_array(self):
        self.output()
        return self.result
