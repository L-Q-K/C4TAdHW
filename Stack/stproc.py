from stack import Stack

class StringProcessor:
    def __init__(self):
        self.stack = Stack()
        self.items = []

    def reverse(self, string):
        res = ''
        for i in string:
            res = i + res
        return res

    def process_sequence(self, string):
        self.items = []

        for i in string:
            if i!= '*':
                self.items.append(i)
            elif (i!= '') and (len(self.items)>=1):
                self.items.pop(-1)

        res = ''
        for i in self.items:
            res = res + i

        return res

    def is_balanced(self, string):
        # self.items = string
        #
        # if (self.items[0] != '{') or (self.items[-1] != '}'):
        #     return False
        #
        # d = 0
        # for i in range(len(self.items)):
        #     if self.items[i] == '{':
        #         d += 1
        #     elif self.items[i] == '}':
        #         d -= 1
        #
        # if d == 0:
        #     return True
        # else:
        #     return False

        for i in string:
            if i == '{':
                self.stack.push(i)
            elif i == '}':
                if not self.stack.is_empty():
                    self.stack.pop()
                else:
                    return False

        if self.stack.is_empty():
            return True

        self.stack.clear()
        return False

    def binary_string(self, string):
        tg = string

        if self.stack.top is not None:
            self.stack.clear()

        while tg//2 != 0:
            self.stack.push(str(tg % 2))
            tg = tg//2

        self.stack.push(str(tg % 2))

        return self.reverse(self.stack.__str__())


st = Stack()

