class Queue:
    def __init__(self, cap):
        self.items = []
        self.capacity = cap

    def __str__(self):
        res = ""
        if self.is_empty():
            return ''

        for item in self.items:
            res += str(item) + ' '

        return res[:-1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def insert(self, item):
        if not self.is_full():
            self.items.insert(0, item)
            return True
        else:
            return False

    def remove(self):
        return self.items.pop()

    def is_full(self):
        return len(self.items) == self.capacity

    def cler(self):
        self.items = []
