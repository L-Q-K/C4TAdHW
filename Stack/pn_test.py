from pn import PolishNotation

p = PolishNotation()

assert hasattr(p, "__init__"), "there are attribute(s) unimplemented"
assert hasattr(p, "stack"), "there are attribute(s) unimplemented"
assert hasattr(p, "calculate"), "there are attribute(s) unimplemented"

assert p.calculate("0") == 0, "wrong answer"
assert p.calculate("77+") == 14, "wrong answer"
assert p.calculate("4572+-*") == 16, "wrong answer"
assert p.calculate("34+2*7/") == 2, "wrong answer"
print("you have passed the test")