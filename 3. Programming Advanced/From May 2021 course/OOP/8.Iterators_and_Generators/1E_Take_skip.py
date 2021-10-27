class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.times = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.times > self.count:
            raise StopIteration
        temp = self.start
        self.start += self.step
        self.times += 1
        return temp


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)


