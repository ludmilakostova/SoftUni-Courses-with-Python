class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        result = ""
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        for symbol in self.text:
            encoded_symbol = ord(symbol)+other
            while encoded_symbol < 32:
                encoded_symbol += 95
            while encoded_symbol > 126:
                encoded_symbol -= 95
            result += chr(encoded_symbol)
        return result


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))


