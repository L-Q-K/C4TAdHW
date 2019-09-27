class Counter:
    def __init__(self):
        self.count = 0
    def tick(self):
        self.count += 1
    def reset(self):
        self.__init__()

counters = Counter()