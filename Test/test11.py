day = [1, 3, 5, 17484, 0, -84984, -9]
l = []

def dao_day(day, vt):
    if vt == len(day)-1:
        l.append(day[0])
    else:
        vt += 1
        l.append(day[-vt])
        dao_day(day, vt)

def ucln (a,b):
    if a == b:
        return a
    elif a>b:
        return ucln(a-b, b)
    elif a<b:
        return ucln(a, b-a)

def gt(dem, max, t):
    t *= dem
    if max == 1:
        return 1
    elif dem == max:
        return t
    else:
        return gt(dem + 1, max, t)

def fib(so):
    if so in [0, 1, 2]:
        return 1
    else:
        return fib(so - 1) + fib(so - 2)

def findMinimum(l):
    if len(l) == 1:
       return l[0]

    else:
       return min(l[0], findMinimum(l[1:]))

print(findMinimum(day))

print(fib(5))
print(ucln(12, 24))
dao_day(day, 0)
print(l)
print(gt(2, int(input('So can tinh: ')), 1))
