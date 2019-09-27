from linkedlist import LinkedList
from linkedlist import Node

n = Node(None, None)
assert(hasattr(n, "content"))
assert(hasattr(n, "next"))

l = LinkedList()
assert(hasattr(l, "head"))
assert(hasattr(l, "__str__"))
assert(hasattr(l, "add_first"))
assert(hasattr(l, "add_last"))
assert(hasattr(l, "remove_first"))
assert(hasattr(l, "remove_last"))
assert(hasattr(l, "find"))

assert(l.__str__() == "<<E>>")

l.add_first(10)
assert(l.__str__() == "10")

l.add_first(5)
assert(l.__str__() == "5->10")

l.add_first(25)
assert(l.__str__() == "25->5->10")

l.add_first(3)
assert(l.__str__() == "3->25->5->10")

l.remove_first()
assert(l.__str__() == "25->5->10")

l.remove_first()
assert(l.__str__() == "5->10")

l.remove_first()
assert(l.__str__() == "10")

l.remove_first()
assert(l.__str__() == "<<E>>")

l.remove_first()
assert(l.__str__() == "<<E>>")

l.add_last(9)
assert(l.__str__() == "9")

l.add_last(21)
assert(l.__str__() == "9->21")

l.add_last(3)
assert(l.__str__() == "9->21->3")

l.add_last(7)
assert(l.__str__() == "9->21->3->7")

l.remove_last()
assert(l.__str__() == "9->21->3")

l.remove_last()
assert(l.__str__() == "9->21")

l.remove_last()
assert(l.__str__() == "9")

l.remove_last()
assert(l.__str__() == "<<E>>")

l.remove_last()
assert(l.__str__() == "<<E>>")

for i in range(4):
  l.add_last(i)
assert(l.__str__() == "0->1->2->3")
n = l.find(-2)
assert(n is None)
n = l.find(2)
assert(n is not None)
assert(n.content == 2)
assert(n.next is not None)
assert(n.next.content == 3)