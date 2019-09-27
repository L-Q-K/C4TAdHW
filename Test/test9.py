import math

def quadro(a,b,c):
    delt = b*b - 4*a*c

    if delt<0:
        print('vo nghiem')
    elif delt == 0:
        print('Nghiem: ' + str(-b/(2*a)))
    else:
        print('Nghiem 1: ' + str((-b-math.sqrt(delt))/(2*a)))
        print('Nghiem 2: ' + str((-b+math.sqrt(delt))/(2*a)))

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

quadro(a, b, c)
