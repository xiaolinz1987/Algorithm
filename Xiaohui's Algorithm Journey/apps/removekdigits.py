class MyRemoveKDigits:

    def __init__(self, num, k):
        self.num = num
        self.k = k
        self.result = None

    def reset(self, num, k):
        self.num = num
        self.k = k
        self.result = None

    def remove_v1(self):
        for i in range(0, self.k):
            has_cut = False
            for j in range(0, len(self.num)-1):
                if self.num[j] > self.num[j+1]:
                    self.num = self.num[0:j] + self.num[j+1:len(self.num)]
                    has_cut = True
                    break

            if not has_cut:
                self.num = self.num[0:len(self.num)-1]
        
        for j in range(0, len(self.num)-1):
            if self.num[0] != '0':
                break
            self.num = self.num[1:len(self.num)]

        if len(self.num) == 0:
            self.result = "0"
            return

        self.result = self.num

    def remove_v2(self):
        new_len = len(self.num) - self.k
        stack = []

        for i in range(0, len(self.num)):
            c = self.num[i]
            while len(stack) > 0 and stack[len(stack)-1] > c and self.k > 0:
                stack.pop()
                self.k -= 1
            
            if '0' == c and len(stack) == 0:
                new_len -= 1
                if new_len < 1:
                    self.result = "0"
                    return
                continue

            stack.append(c)

        if new_len < 1:
            self.result = "0"
            return

        self.result = "".join(stack)

    def output(self):
        print(self.result)

removekdigits = MyRemoveKDigits("1593212", 3)
removekdigits.remove_v1()
print("remove_k_digits_v1:")
removekdigits.output()
removekdigits.reset("30200", 1)
removekdigits.remove_v1()
removekdigits.output()
removekdigits.reset("10", 2)
removekdigits.remove_v1()
removekdigits.output()
removekdigits.reset("1593212", 3)
removekdigits.remove_v2()
print("remove_k_digits_v2:")
removekdigits.output()

        
