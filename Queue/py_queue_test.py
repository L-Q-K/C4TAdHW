from my_queue import Queue

q = Queue(3)
assert(q.is_empty())
assert(hasattr(q, "items"))
assert(hasattr(q, "insert"))
assert(hasattr(q, "remove"))
assert(hasattr(q, "is_empty"))

result = q.insert(5)
assert(result == True)
assert(not q.is_empty())
assert(q.__str__() == "5")

result = q.insert(7)
assert(result == True)
assert(not q.is_empty())
assert(q.__str__() == "7 5")

result = q.insert(-1)
assert(result == True)
assert(not q.is_empty())
assert(q.__str__() == "-1 7 5")

result = q.insert(20)
assert(result == False)
assert(not q.is_empty())
assert(q.__str__() == "-1 7 5")

result = q.insert(33)
assert(result == False)
assert(not q.is_empty())
assert(q.__str__() == "-1 7 5")

x = q.remove()
assert(not q.is_empty())
assert(q.__str__() == "-1 7")
assert(x == 5)

x = q.remove()
assert(not q.is_empty())
assert(q.__str__() == "-1")
assert(x == 7)

q.insert(11)
assert(not q.is_empty())
assert(q.__str__() == "11 -1")

x = q.remove()
assert(not q.is_empty())
assert(q.__str__() == "11")
assert(x == -1)

x = q.remove()
assert(q.is_empty())
assert(q.__str__() == "")
assert(x == 11)