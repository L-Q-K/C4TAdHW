class Stack:
    def __init__(self):
        self.items = [None] * 1000
        self.top = -1

    def __str__(self):
        res = ""
        if (self.top == -1):
            return ""
        for i in range(self.top):
            res += str(self.items[i])
        res += str(self.items[self.top])
        return res

    def push(self, value):
        self.top += 1
        self.items[self.top] = value

    def pop(self):
        if self.is_empty():
            return None
        res = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return res

    def peek(self):
        return self.items[self.top]

    def clear(self):
        self.items = [None] * 1000
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
