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

