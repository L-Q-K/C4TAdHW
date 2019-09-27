from stproc import StringProcessor

proc = StringProcessor()

assert hasattr(proc, "__init__"), "__init__ method not implemented"
assert hasattr(proc, "stack"), "stack property not found"

point = 0
passed = 0


if hasattr(proc, "reverse"):
    print("Testing reverse method")
    if proc.reverse("abcdef") == "fedcba":
        point += 1
    if proc.reverse("abccba") == "abccba":
        point += 1

if hasattr(proc, "process_sequence"):
    print("testing process_sequence method")
    if proc.process_sequence("ab*de*abcdef") == "adabcdef":
        point += 2
    if proc.process_sequence("d*e*f*g*") == "":
        point += 2
    if proc.process_sequence("d****ef") == "ef":
        point += 2

if hasattr(proc, "is_balanced"):
    print("testing is_balanced method")
    if proc.is_balanced("{{{}}}"):
        point += 3
    if not proc.is_balanced("{{{}"):
        point += 3
    if not proc.is_balanced("}}{{"):
        point += 3
    if proc.is_balanced("{{{}}{}{}}"):
        point += 3

if hasattr(proc, "binary_string"):
    print("testing binary_string method")
    if proc.binary_string(124) == "1111100":
        point += 4
    if proc.binary_string(10) == proc.binary_string(10):
        point += 4
    if proc.binary_string(697) == "1010111001":
        point += 4


print(f"you passed the test with {point}/32 points")
