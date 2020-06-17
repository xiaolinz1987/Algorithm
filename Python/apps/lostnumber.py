class MyLostNumber:

    def __init__(self, input_array):
        self.array = input_array
        self.result = [0] * 2

    def calculate(self):
        xor_result = 0
        for i in range(0, len(self.array)):
            xor_result ^= self.array[i]

        if xor_result == 0:
            raise ValueError

        separator = 1
        while 0 == (xor_result & separator):
            separator <<= 1

        for i in range(0, len(self.array)):
            if 0 == (self.array[i] & separator):
                self.result[0] ^= self.array[i]
            else:
                self.result[1] ^= self.array[i]

    def get_lost_number(self):
        return self.result

