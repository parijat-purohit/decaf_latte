class TextInput:
    def __init__(self):
        self.val = ''

    def add(self, chr):
        self.val += chr

    def get_value(self):
        return self.val


class NumericInput(TextInput):
    def add(self, chr):
        if '0' <= chr <= '9':
            self.val += chr


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())
