from polynom import TermNode, Polynom

t = TermNode(3, 4, None)
assert(hasattr(t, "coefficient"))
assert(hasattr(t, "degree"))
assert(hasattr(t, "next"))
assert(hasattr(t, "evaluate"))
assert(t.__str__() == "3x^4")

t.coefficient = 0
assert(t.__str__() == "")
assert(t.evaluate(100) == 0)

t.coefficient = 3
t.degree = 1
assert(t.__str__() == "3x")
assert(t.evaluate(2) == 6)

t.coefficient = 4
t.degree = 2
assert(t.__str__() == "4x^2")
assert(t.evaluate(3) == 36)

t.coefficient = 1
t.degree = 2
assert(t.__str__() == "x^2")
assert(t.evaluate(3) == 9)

p = Polynom()
assert(hasattr(p, "head"))
assert(hasattr(p, "add"))
assert(hasattr(p, "evaluate"))

assert(p.__str__() == "")
assert(p.evaluate(100) == 0)

p.add(4, 3)
assert(p.__str__() == "4x^3")
assert(p.evaluate(2) == 32)

p.add(3, 2)
assert(p.__str__() == "4x^3+3x^2")
assert(p.evaluate(2) == 32+12)

p.add(1, 5)
assert(p.__str__() == "x^5+4x^3+3x^2")
assert(p.evaluate(2) == 32+32+12)

p2 = p.derivate()
assert(p2.__str__() == "5x^4+12x^2+6x")