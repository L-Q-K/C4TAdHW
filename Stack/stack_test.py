from stproc import Stack

s = Stack()
assert(s.is_empty())
assert(hasattr(s, "items"))
assert(hasattr(s, "push"))
assert(hasattr(s, "top"))
assert(hasattr(s, "pop"))
assert(hasattr(s, "peek"))
assert(hasattr(s, "is_empty"))
assert(hasattr(s, "clear"))

s.push(5)
assert(not s.is_empty())
assert(s.__str__() == "5")

s.push(7)
assert(not s.is_empty())
assert(s.peek() == 7)
assert(s.__str__() == "5 7")

s.push(-1)
assert(not s.is_empty())
assert(s.peek() == -1)
assert(s.__str__() == "5 7 -1")

x = s.pop()
assert(not s.is_empty())
assert(s.__str__() == "5 7")
assert(s.peek() == 7)
assert(x == -1)

x = s.pop()
assert(not s.is_empty())
assert(s.__str__() == "5")
assert(x == 7)

s.push(11)
assert(not s.is_empty())
assert(s.__str__() == "5 11")

x = s.pop()
assert(not s.is_empty())
assert(s.__str__() == "5")
assert(x == 11)

x = s.pop()
assert(s.is_empty())
assert(s.__str__() == "")
assert(x == 5)

assert(s.pop() is None)
assert(s.is_empty())
assert(s.__str__() == "")

s.push(6)
s.push(7)
assert(s.__str__() == "6 7")
s.clear()
assert(s.__str__() == "")
assert(s.is_empty())

print("you passed the test")