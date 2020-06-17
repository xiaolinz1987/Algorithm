class MyMedianSortedArray:

    def __init__(self, input_array_1, input_array_2):
        self.array1 = input_array_1
        self.array2 = input_array_2
        self.median = 0

    def calculate(self):
        m, n = len(self.array1), len(self.array2)
        if m > n:
            self.array1, self.array2, m, n = self.array2, self.array1, n, m
        if n == 0:
            raise ValueError

        start, end, half_len = 0, m, (m + n + 1)//2
        while start <= end:
            i = (start + end)//2
            j = half_len - i

            if i < m and self.array2[j-1] > self.array1[i]:
                start = i + 1
            elif i > 0 and self.array1[i-1] > self.array2[j]:
                end = i - 1
            else:
                if i == 0:
                    max_of_left = self.array2[j-1]
                elif j == 0:
                    max_of_left = self.array1[i-1]
                else:
                    max_of_left = max(self.array1[i-1], self.array2[j-1])

                if (m + n)%2 == 1:
                    self.median = max_of_left
                    return

                if i == m:
                    min_of_right = self.array2[j]
                elif j == n:
                    min_of_right = self.array1[i]
                else:
                    min_of_right = min(self.array1[i], self.array2[j])

                self.median = (max_of_left + min_of_right) / 2.0
                return

    def get_median(self):
        return self.median

