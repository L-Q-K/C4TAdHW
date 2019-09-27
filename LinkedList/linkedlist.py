class Node:
    def __init__(self, cont, next):
        self.content = cont
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        res = ""
        if self.head == None:
            return "<<E>>"

        curr = self.head
        while curr != None:
            res += str(curr.content) + '->'
            curr = curr.next
        return res[:-2]
    def add_first(self, add_cont):
        node = Node(add_cont, None)
        node.next = self.head
        self.head = node
    def remove_first(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
    def add_last(self, content):
        node = Node(content, None)

        curr = self.head
        if self.head == None:
            self.head = node
            return '0'

        while curr.next != None:
            curr = curr.next

        curr.next = node
    def remove_last(self):
        curr = self.head

        if curr == None:
            return None
        if curr.next == None:
            self.head = None
            return curr
        if curr.next.next == None:
            temp = curr.next
            curr.next = None
            return temp

        while curr.next.next != None:
            curr = curr.next

        temp = curr.next
        curr.next = None
        return temp
    def find(self, cont):
        if self.head == None:
            return None

        curr = self.head

        while curr != None:
            if curr.content == cont:
                return curr
            curr = curr.next

        return None


