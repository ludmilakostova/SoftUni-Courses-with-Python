class vowels:
    def __init__(self, string):
        self.string = string
        self.start = 0
        self.vowels = "AEOUIYaeouiy"
        self.vowels_string = [el for el in self.string if el in self.vowels]
        self.end = len(self.vowels_string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowels_string[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
