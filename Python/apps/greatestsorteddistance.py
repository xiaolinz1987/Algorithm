class MyBucket:

    def __init__(self):
        self.max = None
        self.min = None

class MyGreatestSortedDistance:

    def __init__(self, input_array):
        self.array = input_array
        self.greatest_sorted_distance = 0

    def calcuate(self):
        max_value = self.array[0]
        min_value = self.array[0]
        for i in range(1, len(self.array)):
            if self.array[i] > max_value:
                max_value = self.array[i]
            if self.array[i] < min_value:
                min_value = self.array[i]

        d = max_value - min_value
        if d == 0:
            return

        bucket_num = len(self.array)
        buckets = []
        for i in range(0, bucket_num):
            buckets.append(MyBucket())

        for i in range(0, len(self.array)):
            index = int((self.array[i] - min_value) * (bucket_num - 1) / d)
            if buckets[index].min is None or buckets[index].min > self.array[i]:
                buckets[index].min = self.array[i]
            if buckets[index].max is None or buckets[index].max < self.array[i]:
                buckets[index].max = self.array[i]

        left_max = buckets[0].max
        for i in range(1, len(buckets)):
            if buckets[i].min is None:
                continue
            if buckets[i].min - left_max > self.greatest_sorted_distance:
                self.greatest_sorted_distance = buckets[i].min - left_max
            left_max = buckets[i].max
    
    def output(self):
        print(self.greatest_sorted_distance)

array = list([2, 6, 3, 5, 6, 10, 9])
distance = MyGreatestSortedDistance(array)
distance.calcuate()
distance.output()

