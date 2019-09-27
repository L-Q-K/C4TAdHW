def reversed(self, string):
    res = ''
    for i in string:
        res = i + res
    return res


def process_sequence(self, string):
    self.items = []

    for i in string:
        if i != '*':
            self.items.append(i)
        else:
            self.items.pop(-1)
    res = ''
    for i in self.items:
        res = res + i

    return res


def is_balanced(self, string):
    self.items = string

    if (self.items[0] != '{') or (self.items[-1] != '}'):
        return False

    d = 0
    for i in range(len(self.items)):
        if self.items[i] == '{':
            d += 1
        elif self.items[i] == '}':
            d -= 1

    if d == 0:
        return True
    else:
        return False


def binary_string(selfs, string):
    tg = string
    res = ''

    while tg // 2 != 0:
        res = str(tg % 2) + res
        tg = tg // 2

    res = str(tg % 2) + res

    return res