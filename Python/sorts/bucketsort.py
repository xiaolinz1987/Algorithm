class MyBucketSort:

    def __init__(self, input_array):
        self.array = input_array
        self.sorted_array = []

    def get_array(self):
        return self.sorted_array

    def bucket_sort(self):
        max_value = self.array[0]
        min_value = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] > max_value:
                max_value = self.array[i]
            if self.array[i] < min_value:
                min_value = self.array[i]

        d = max_value - min_value
        bucket_num = len(self.array)
        bucket_list = []
        for i in range(0, bucket_num):
            bucket_list.append([])

        for i in range(0, len(self.array)):
            num = int((self.array[i] - min_value) * (bucket_num - 1) / d)
            bucket = bucket_list[num]
            bucket.append(self.array[i])

        for i in range(0, len(bucket_list)):
            bucket_list[i].sort()

        for sub_list in bucket_list:
            for element in sub_list:
                self.sorted_array.append(element)

