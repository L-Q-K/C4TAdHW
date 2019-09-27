class TermNode:
    def __init__(self, coefficient, degree, next):
        self.coefficient = coefficient
        self.degree = degree
        self.next = next
    def evaluate(self, x):
        return self.coefficient*x**self.degree
    def __str__(self):
        if self.coefficient == 0:
            return ''

        res = str(self.coefficient) + 'x^' + str(self.degree)

        if self.degree == 1:
            return res[:-2]
        if self.coefficient == 1:
            return res[1:]
        if self.degree == 0:
            return self.coefficient
        return res

class Polynom:
    def __init__(self):
        self.head = None

    def __str__(self):
        res = ""
        if self.head == None:
            return ""

        curr = self.head
        while curr is not None:
            if curr.degree == 0:
                res += '1+'
            else:
                coe = str(curr.coefficient)
                deg = str(curr.degree)
                if coe == '1':
                    coe = ''
                if deg == '0':
                    res += '1+'
                    break
                elif deg == '1':
                    deg = ''
                else:
                    deg = '^' + deg

                res += coe + 'x' + deg + '+'
            curr = curr.next
        return res[:-1]

    def add(self,c,d):
        curr = self.head
        prev = self.head
        if curr is None:
            self.head = TermNode(c,d, None)
            return ''

        while curr is not None:
            if (curr.degree < d):
                node = TermNode(c, d, None)
                node.next = curr
                if curr is not self.head:
                    prev.next = node
                else:
                    self.head = node
                break
            elif (curr.degree == d):
                curr.coefficient += c
                break
            else:
                if curr.next is None:
                    node = TermNode(c, d, None)
                    curr.next = node
                    break
                prev = curr
                curr = curr.next

    def evaluate(self, x):
        curr = self.head

        if curr is None:
            return 0

        t = 0
        while curr is not None:
            t += curr.evaluate(x)
            curr = curr.next

        return t

    def derivate(self):
        curr = self.head

        if curr is None:
            return

        p = Polynom()
        while curr is not None:

            p.add(curr.coefficient*curr.degree, curr.degree-1)
            curr = curr.next

        return p



