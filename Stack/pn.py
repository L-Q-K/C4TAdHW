from stproc import Stack

class PolishNotation:
    def __init__(self):
        self.stack = Stack()

    def calculate(self, string):
        i = 0
        for i in range(len(string)):
            if string[i] not in ['+', '-', '*', '/']:
                self.stack.push(string[i])
            elif string[i] in ['+', '-', '*', '/']:
                t = 0
                if string[i] == '+':
                    t = int(self.stack.items[self.stack.top]) + int(self.stack.items[self.stack.top - 1])
                elif string[i] == '-':
                    t = int(self.stack.items[self.stack.top]) - int(self.stack.items[self.stack.top - 1])
                elif string[i] == '*':
                    t = int(self.stack.items[self.stack.top]) * int(self.stack.items[self.stack.top - 1])
                elif string[i] == '/':
                    t = int(self.stack.items[self.stack.top - 1]) // int(self.stack.items[self.stack.top])

                for i in range(2):
                    self.stack.pop()

                self.stack.push(t)
        return int(self.stack.items[self.stack.top])

st = PolishNotation()




