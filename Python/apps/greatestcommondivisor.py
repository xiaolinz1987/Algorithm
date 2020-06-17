class MyGreatestCommonDivisor:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.greatest_common_divisor = 1

    def set(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate_v1(self):
        big = max(self.num1, self.num2)
        small = min(self.num1, self.num2)
        if big % small == 0:
            self.greatest_common_divisor = small
            return

        for i in range(small//2, 1, -1):
            if small % i == 0 and big % i == 0:
                self.greatest_common_divisor = i
                return

    def __calculate_v2_core(self, num1, num2):
        big = max(num1, num2)
        small = min(num1, num2)
        if big % small == 0:
            return small

        return self.__calculate_v2_core(big % small, small)

    def calculate_v2(self):
        self.greatest_common_divisor = self.__calculate_v2_core(self.num1, self.num2)

    def __calculate_v3_core(self, num1, num2):
        if num1 == num2:
            return num1

        big = max(num1, num2)
        small = min(num1, num2)
        return self.__calculate_v3_core(big - small, small)

    def calculate_v3(self):
        self.greatest_common_divisor = self.__calculate_v3_core(self.num1, self.num2)

    def __calculate_v4_core(self, num1, num2):
        if num1 == num2:
            return num1

        if (num1 & 1) == 0 and (num2 & 1) == 0:
            return self.__calculate_v4_core(num1 >> 1, num2 >> 1) << 1
        elif (num1 & 1) == 0 and (num2 & 1) != 0:
            return self.__calculate_v4_core(num1 >> 1, num2)
        elif (num1 & 1) != 0 and (num2 & 1) == 0:
            return self.__calculate_v4_core(num1, num2 >> 1)
        else:
            big = max(num1, num2)
            small = min(num1, num2)
            return self.__calculate_v4_core(big - small, small)

    def calculate_v4(self):
        self.greatest_common_divisor = self.__calculate_v4_core(self.num1, self.num2)

    def power_of_2(self):
        return (self.greatest_common_divisor & self.greatest_common_divisor-1) == 0

    def get_greatest_common_divisor(self):
        return self.greatest_common_divisor

