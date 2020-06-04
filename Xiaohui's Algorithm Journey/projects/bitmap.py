class MyBitmap:

    def __init__(self, size):
        self.bit_size = size
        self.word_size = self.get_word_index(size-1) + 1
        self.words = [0] * self.word_size
        
    def __assert(self, bit_index):
        if bit_index < 0 or bit_index > self.bit_size - 1:
            raise Exception("Out of range!")

    def reset(self, size):
        self.bit_size = size
        self.word_size = self.get_word_index(size-1) + 1
        self.words = [0] * self.word_size

    def get_word_index(self, bit_index):
        return bit_index >> 6

    def get_word_size(self):
        return self.word_size

    def get_bit(self, bit_index):
        self.__assert(bit_index)        
        word_index = self.get_word_index(bit_index)
        return (self.words[word_index] & (1 << bit_index)) != 0

    def set_bit(self, bit_index):
        self.__assert(bit_index)
        word_index = self.get_word_index(bit_index)
        self.words[word_index] |= (1 << bit_index)

bit1 = MyBitmap(128)
bit1.set_bit(126)
bit1.set_bit(75)
print(bit1.get_bit(126))
print(bit1.get_bit(75))
print(bit1.get_bit(112))

bit1.reset(10)
bit1.set_bit(1)
bit1.set_bit(2)
bit2 = MyBitmap(10)
bit2.set_bit(1)
bit2.set_bit(3)

word_size_1 = bit1.get_word_size()
word_size_2 = bit2.get_word_size()

word_size = min(word_size_1, word_size_2)
intersection = [0] * word_size
print("Intersection:")
for i in range(0, word_size):
    intersection[i] = bit1.words[i] & bit2.words[i]
    print(bin(intersection[i]))

union = [0] * word_size
print("Union:")
for i in range(0, word_size):
    union[i] = bit1.words[i] | bit2.words[i]
    print(bin(union[i]))
if word_size_1 > word_size_2:
    for i in range(word_size, word_size_1):
        union[i] = bit1.words[i]
        print(bin(union[i]))
else:
    for i in range(word_size, word_size_2):
        union[i] = bit2.words[i]
        print(bin(union[i]))

