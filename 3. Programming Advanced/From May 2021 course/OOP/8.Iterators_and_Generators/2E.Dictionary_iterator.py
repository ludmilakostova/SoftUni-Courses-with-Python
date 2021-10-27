class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0
        self.result = [(key, value) for key, value in self.dictionary.items()]
        self.end = len(self.dictionary) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.end:
            raise StopIteration
        temp = self.result[self.index]
        self.index += 1
        return temp


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
