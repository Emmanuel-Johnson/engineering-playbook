class SkipIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        value = self.data[self.index]
        self.index += 2   # skip every second element
        return value


nums = [1, 2, 3, 4, 5, 6]

for i in SkipIterator(nums):
    print(i)